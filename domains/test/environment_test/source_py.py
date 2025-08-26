#!/usr/bin/env python3
"""ZAAI Environment Test - Python Source File

This module serves as a comprehensive test file for validating the ZAAI system's
ability to process Python source code files. It demonstrates various Python
language features, programming patterns, and best practices while following
the AI-first documentation philosophy established in the ZAAI codebase.

Architecture Purpose:
This file is referenced by the test domain (domains/test/test.yaml) to validate
that the ZAAI environment can properly load, parse, and understand Python
source files. It serves as both a test artifact and a demonstration of
comprehensive Python programming capabilities.

Cross-file Dependencies:
- Referenced by: domains/test/test.yaml (env benchmark)
- Used by: Environment test functions that validate file loading capabilities
- Part of: ZAAI environment validation test suite

File Format Validation:
- Encoding: UTF-8 with proper Python shebang
- Syntax: Valid Python 3.8+ compatible code
- Documentation: Complete docstrings following Google/PEP 257 standards
- Type Hints: Full type annotations for AI readability

Testing Philosophy:
This file contains representative code that an AI system should be able to
understand, parse, and potentially modify. It includes common programming
patterns, error handling, and documentation standards that serve as a
benchmark for code comprehension capabilities.
"""

import asyncio
import json
import logging
import sqlite3
import threading
import time
from abc import ABC, abstractmethod
from collections import defaultdict, namedtuple
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum, auto
from pathlib import Path
from typing import Any, Dict, List, Optional, Protocol, Union
from urllib.parse import urlparse


# Constants Section - Following AI-first documentation philosophy of named constants
class SystemConstants:
    """System-wide constants for the Python test application.
    
    These constants eliminate magic numbers and provide semantic meaning
    to all numeric and string values used throughout the application.
    This follows the AI-first documentation principle of making all
    values explicit and understandable.
    """
    APP_NAME: str = "Python Environment Test Application"
    APP_VERSION: str = "1.0.0"
    DEFAULT_PORT: int = 8080
    MAX_RETRY_ATTEMPTS: int = 3
    DEFAULT_TIMEOUT_SECONDS: int = 30
    MAX_USERS_IN_MEMORY: int = 1000
    LOG_FORMAT: str = "[%(asctime)s] %(levelname)s: %(message)s"
    DATABASE_FILE: str = "test_users.db"
    
    # Error handling constants
    NETWORK_TIMEOUT_SECONDS: int = 10
    RETRY_DELAY_SECONDS: float = 1.0
    
    # Data processing constants  
    BATCH_SIZE: int = 100
    MAX_STRING_LENGTH: int = 255


# Type Definitions - Explicit type aliases for AI comprehension
UserId = int
Timestamp = float
ConfigDict = Dict[str, Any]
UserData = Dict[str, Union[str, int, bool, None]]


# Enums - Strongly typed enumeration for state management
class UserStatus(Enum):
    """User account status enumeration.
    
    Defines the possible states for a user account in the system.
    Using enums provides type safety and makes state transitions
    explicit and traceable for AI analysis.
    """
    ACTIVE = auto()
    INACTIVE = auto()
    PENDING = auto()
    SUSPENDED = auto()


class LogLevel(Enum):
    """Logging level enumeration for structured logging.
    
    Provides explicit log level definitions that can be understood
    and manipulated by AI systems for log analysis and debugging.
    """
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


# Named Tuples - Structured data containers
UserPreferences = namedtuple('UserPreferences', [
    'theme', 'notifications', 'language', 'timezone'
])

DatabaseConnection = namedtuple('DatabaseConnection', [
    'connection', 'cursor', 'is_active'
])


# Dataclasses - Modern Python data structures with full documentation
@dataclass
class User:
    """Represents a user entity in the system.
    
    This dataclass encapsulates all user-related data and provides
    a clean interface for user management operations. The class
    includes comprehensive type hints and validation logic.
    
    Attributes:
        id: Unique identifier for the user
        name: Full display name of the user
        email: Email address (must be valid format)
        age: Optional age in years (must be positive if provided)
        status: Current account status from UserStatus enum
        preferences: User preferences configuration
        created_at: Timestamp when user was created
        metadata: Additional key-value data storage
        
    Example:
        >>> user = User(
        ...     id=1,
        ...     name="Alice Johnson",
        ...     email="alice@example.com",
        ...     age=28,
        ...     status=UserStatus.ACTIVE
        ... )
        >>> print(user.is_adult())
        True
    """
    id: UserId
    name: str
    email: str
    age: Optional[int] = None
    status: UserStatus = UserStatus.PENDING
    preferences: UserPreferences = field(
        default_factory=lambda: UserPreferences(
            theme='light',
            notifications=True,
            language='en',
            timezone='UTC'
        )
    )
    created_at: Timestamp = field(default_factory=time.time)
    metadata: ConfigDict = field(default_factory=dict)
    
    def __post_init__(self) -> None:
        """Validate user data after initialization.
        
        Performs comprehensive validation of user data to ensure
        data integrity. This method is called automatically after
        the dataclass is initialized.
        
        Raises:
            ValueError: If email format is invalid or age is negative
        """
        if not self._is_valid_email(self.email):
            raise ValueError(f"Invalid email format: {self.email}")
        
        if self.age is not None and self.age < 0:
            raise ValueError(f"Age cannot be negative: {self.age}")
    
    def is_adult(self) -> bool:
        """Check if user is an adult (18 or older).
        
        Returns:
            bool: True if user is 18 or older, False otherwise.
                  Returns False if age is not specified.
        """
        return self.age is not None and self.age >= 18
    
    def update_status(self, new_status: UserStatus) -> None:
        """Update the user's account status.
        
        Args:
            new_status: The new status to set for the user
            
        Example:
            >>> user.update_status(UserStatus.SUSPENDED)
            >>> assert user.status == UserStatus.SUSPENDED
        """
        self.status = new_status
    
    def to_dict(self) -> UserData:
        """Convert user object to dictionary representation.
        
        Creates a dictionary representation suitable for JSON serialization
        or database storage. Handles enum conversion and datetime formatting.
        
        Returns:
            dict: Dictionary containing all user data with JSON-compatible types
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'age': self.age,
            'status': self.status.name,
            'preferences': self.preferences._asdict(),
            'created_at': self.created_at,
            'metadata': self.metadata
        }
    
    @staticmethod
    def _is_valid_email(email: str) -> bool:
        """Validate email address format.
        
        Performs basic email validation to ensure the address contains
        required components. This is a simplified validation suitable
        for testing purposes.
        
        Args:
            email: Email address string to validate
            
        Returns:
            bool: True if email format appears valid, False otherwise
        """
        return '@' in email and '.' in email and len(email) > 5


# Protocol Definitions - Interface contracts for AI understanding
class Repository(Protocol):
    """Repository interface for data access operations.
    
    This protocol defines the contract for data repository implementations.
    Using protocols allows for flexible implementations while maintaining
    type safety and clear interface expectations for AI analysis.
    """
    
    def save(self, user: User) -> UserId:
        """Save a user to the repository.
        
        Args:
            user: User object to save
            
        Returns:
            UserId: The ID assigned to the saved user
            
        Raises:
            RepositoryError: If save operation fails
        """
        ...
    
    def find_by_id(self, user_id: UserId) -> Optional[User]:
        """Find a user by their ID.
        
        Args:
            user_id: Unique identifier for the user
            
        Returns:
            Optional[User]: User object if found, None otherwise
        """
        ...
    
    def find_all(self) -> List[User]:
        """Retrieve all users from the repository.
        
        Returns:
            List[User]: List of all user objects
        """
        ...
    
    def delete(self, user_id: UserId) -> bool:
        """Delete a user from the repository.
        
        Args:
            user_id: Unique identifier for the user to delete
            
        Returns:
            bool: True if user was deleted, False if not found
        """
        ...


class Logger(Protocol):
    """Logging interface for structured logging operations.
    
    Defines the contract for logging implementations, ensuring
    consistent logging behavior across the application.
    """
    
    def log(self, level: LogLevel, message: str, **kwargs: Any) -> None:
        """Log a message at the specified level.
        
        Args:
            level: Logging level from LogLevel enum
            message: The message to log
            **kwargs: Additional context data for structured logging
        """
        ...


# Custom Exception Classes - Comprehensive error handling
class ApplicationError(Exception):
    """Base exception class for application-specific errors.
    
    Provides a foundation for all application exceptions with
    structured error information and context preservation.
    """
    
    def __init__(self, message: str, error_code: str = "UNKNOWN", 
                 context: Optional[Dict[str, Any]] = None) -> None:
        """Initialize application error with context.
        
        Args:
            message: Human-readable error description
            error_code: Structured error code for programmatic handling
            context: Additional context information for debugging
        """
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.context = context or {}
        self.timestamp = time.time()


class RepositoryError(ApplicationError):
    """Exception raised for repository operation failures.
    
    Specialized exception for data access layer errors,
    providing specific context for database and storage issues.
    """
    pass


class ValidationError(ApplicationError):
    """Exception raised for data validation failures.
    
    Used when input data fails validation checks,
    providing specific information about validation failures.
    """
    pass


# Repository Implementation - Concrete data access layer
class InMemoryUserRepository:
    """In-memory implementation of user repository.
    
    Provides a simple in-memory storage implementation for testing
    and development purposes. Includes thread safety and comprehensive
    error handling suitable for AI analysis and modification.
    
    This implementation demonstrates:
    - Thread-safe operations using locks
    - Comprehensive error handling and validation
    - Clear separation of concerns
    - Extensive documentation for AI comprehension
    
    Thread Safety:
    All public methods are protected by a threading lock to ensure
    thread-safe operations in concurrent environments.
    
    Memory Management:
    Includes memory usage tracking and limits to prevent excessive
    memory consumption during testing operations.
    """
    
    def __init__(self, max_users: int = SystemConstants.MAX_USERS_IN_MEMORY) -> None:
        """Initialize the in-memory repository.
        
        Args:
            max_users: Maximum number of users to store in memory
        """
        self._users: Dict[UserId, User] = {}
        self._next_id: UserId = 1
        self._max_users = max_users
        self._lock = threading.RLock()
        self._created_at = time.time()
        
    def save(self, user: User) -> UserId:
        """Save a user to the in-memory repository.
        
        Thread-safe method to save or update a user in the repository.
        Assigns a new ID if the user doesn't have one, or updates
        existing user if ID is already assigned.
        
        Args:
            user: User object to save
            
        Returns:
            UserId: The ID assigned to the saved user
            
        Raises:
            RepositoryError: If repository is at capacity or save fails
            ValidationError: If user data is invalid
        """
        with self._lock:
            if len(self._users) >= self._max_users and user.id not in self._users:
                raise RepositoryError(
                    f"Repository at maximum capacity: {self._max_users}",
                    error_code="CAPACITY_EXCEEDED",
                    context={
                        "current_count": len(self._users),
                        "max_capacity": self._max_users
                    }
                )
            
            # Assign new ID if user doesn't have one
            if user.id == 0 or user.id not in self._users:
                user.id = self._next_id
                self._next_id += 1
            
            # Validate user before saving
            try:
                # This will call __post_init__ validation
                User(**user.to_dict())
            except (ValueError, TypeError) as e:
                raise ValidationError(
                    f"Invalid user data: {e}",
                    error_code="INVALID_USER_DATA",
                    context={"user_data": user.to_dict()}
                )
            
            self._users[user.id] = user
            return user.id
    
    def find_by_id(self, user_id: UserId) -> Optional[User]:
        """Find a user by their unique identifier.
        
        Args:
            user_id: Unique identifier for the user
            
        Returns:
            Optional[User]: User object if found, None if not found
        """
        with self._lock:
            return self._users.get(user_id)
    
    def find_all(self) -> List[User]:
        """Retrieve all users from the repository.
        
        Returns a copy of all users to prevent external modification
        of the internal user storage.
        
        Returns:
            List[User]: List of all user objects (copies)
        """
        with self._lock:
            return list(self._users.values())
    
    def delete(self, user_id: UserId) -> bool:
        """Delete a user from the repository.
        
        Args:
            user_id: Unique identifier for the user to delete
            
        Returns:
            bool: True if user was found and deleted, False otherwise
        """
        with self._lock:
            if user_id in self._users:
                del self._users[user_id]
                return True
            return False
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get repository statistics for monitoring and debugging.
        
        Returns:
            dict: Statistics including user count, memory usage, etc.
        """
        with self._lock:
            status_counts = defaultdict(int)
            adult_count = 0
            total_age = 0
            age_count = 0
            
            for user in self._users.values():
                status_counts[user.status.name] += 1
                if user.is_adult():
                    adult_count += 1
                if user.age is not None:
                    total_age += user.age
                    age_count += 1
            
            return {
                "total_users": len(self._users),
                "status_distribution": dict(status_counts),
                "adult_users": adult_count,
                "minor_users": len(self._users) - adult_count,
                "average_age": total_age / age_count if age_count > 0 else 0,
                "repository_capacity": self._max_users,
                "capacity_utilization": len(self._users) / self._max_users,
                "repository_age_seconds": time.time() - self._created_at,
                "next_available_id": self._next_id
            }


# Service Layer - Business logic implementation
class UserService:
    """User management service with comprehensive business logic.
    
    This service class encapsulates all user-related business operations,
    including user creation, validation, status management, and reporting.
    It demonstrates proper dependency injection, error handling, and
    logging practices for AI comprehension.
    
    Architecture Pattern:
    - Dependency Injection: Repository and logger are injected dependencies
    - Single Responsibility: Focuses solely on user business logic
    - Error Handling: Comprehensive exception handling with context
    - Logging: Structured logging for operational visibility
    
    Thread Safety:
    This service is thread-safe when used with thread-safe repository
    and logger implementations.
    """
    
    def __init__(self, repository: Repository, logger: Logger) -> None:
        """Initialize user service with dependencies.
        
        Args:
            repository: Data access layer implementation
            logger: Logging service implementation
        """
        self._repository = repository
        self._logger = logger
        self._service_started = time.time()
        
        self._logger.log(
            LogLevel.INFO,
            "UserService initialized",
            service_start_time=self._service_started
        )
    
    async def create_user_async(self, name: str, email: str, 
                               age: Optional[int] = None) -> User:
        """Create a new user asynchronously.
        
        Demonstrates async/await patterns for non-blocking operations.
        In a real implementation, this might involve network calls
        to validate email addresses or check for duplicates.
        
        Args:
            name: Full name of the user
            email: Email address (must be unique)
            age: Optional age in years
            
        Returns:
            User: The newly created user object
            
        Raises:
            ValidationError: If input data is invalid
            RepositoryError: If user creation fails
        """
        self._logger.log(
            LogLevel.INFO,
            "Creating new user",
            name=name,
            email=email,
            age=age
        )
        
        # Simulate async validation (e.g., email uniqueness check)
        await asyncio.sleep(0.1)  # Simulated network delay
        
        # Check for existing user with same email
        existing_users = self._repository.find_all()
        for existing_user in existing_users:
            if existing_user.email.lower() == email.lower():
                raise ValidationError(
                    f"User with email {email} already exists",
                    error_code="DUPLICATE_EMAIL",
                    context={
                        "email": email,
                        "existing_user_id": existing_user.id
                    }
                )
        
        # Create new user
        user = User(
            id=0,  # Will be assigned by repository
            name=name,
            email=email,
            age=age,
            status=UserStatus.ACTIVE
        )
        
        try:
            user_id = self._repository.save(user)
            user.id = user_id
            
            self._logger.log(
                LogLevel.INFO,
                "User created successfully",
                user_id=user_id,
                name=name,
                email=email
            )
            
            return user
            
        except Exception as e:
            self._logger.log(
                LogLevel.ERROR,
                "Failed to create user",
                error=str(e),
                name=name,
                email=email
            )
            raise
    
    def get_user_statistics(self) -> Dict[str, Any]:
        """Generate comprehensive user statistics.
        
        Returns:
            dict: Detailed statistics about users in the system
        """
        self._logger.log(LogLevel.DEBUG, "Generating user statistics")
        
        if hasattr(self._repository, 'get_statistics'):
            stats = self._repository.get_statistics()
        else:
            # Fallback implementation for basic repositories
            users = self._repository.find_all()
            stats = self._calculate_basic_statistics(users)
        
        stats['service_uptime_seconds'] = time.time() - self._service_started
        
        self._logger.log(
            LogLevel.INFO,
            "User statistics generated",
            total_users=stats.get('total_users', 0)
        )
        
        return stats
    
    def _calculate_basic_statistics(self, users: List[User]) -> Dict[str, Any]:
        """Calculate basic statistics for users.
        
        Args:
            users: List of users to analyze
            
        Returns:
            dict: Basic statistical information
        """
        if not users:
            return {
                "total_users": 0,
                "status_distribution": {},
                "adult_users": 0,
                "minor_users": 0,
                "average_age": 0
            }
        
        status_counts = defaultdict(int)
        adult_count = 0
        total_age = 0
        age_count = 0
        
        for user in users:
            status_counts[user.status.name] += 1
            if user.is_adult():
                adult_count += 1
            if user.age is not None:
                total_age += user.age
                age_count += 1
        
        return {
            "total_users": len(users),
            "status_distribution": dict(status_counts),
            "adult_users": adult_count,
            "minor_users": len(users) - adult_count,
            "average_age": total_age / age_count if age_count > 0 else 0
        }


# Logger Implementation - Structured logging
class StructuredLogger:
    """Structured logging implementation with JSON output.
    
    Provides structured logging capabilities with JSON formatting
    for machine-readable log output. Includes log level filtering
    and contextual information preservation.
    """
    
    def __init__(self, min_level: LogLevel = LogLevel.INFO) -> None:
        """Initialize structured logger.
        
        Args:
            min_level: Minimum log level to output
        """
        self._min_level = min_level
        self._level_priorities = {
            LogLevel.DEBUG: 0,
            LogLevel.INFO: 1,
            LogLevel.WARNING: 2,
            LogLevel.ERROR: 3,
            LogLevel.CRITICAL: 4
        }
    
    def log(self, level: LogLevel, message: str, **kwargs: Any) -> None:
        """Log a structured message.
        
        Args:
            level: Logging level
            message: Primary log message
            **kwargs: Additional structured data
        """
        if self._level_priorities[level] < self._level_priorities[self._min_level]:
            return
        
        log_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": level.value,
            "message": message,
            "context": kwargs
        }
        
        # In a real implementation, this might write to files or external systems
        print(json.dumps(log_entry, default=str))


# Utility Functions - Helper functions with comprehensive documentation
def fibonacci_generator(n: int) -> List[int]:
    """Generate Fibonacci sequence up to n terms.
    
    Implements the classic Fibonacci sequence generation using
    an iterative approach for efficiency. Includes input validation
    and comprehensive error handling.
    
    Args:
        n: Number of Fibonacci terms to generate (must be non-negative)
        
    Returns:
        List[int]: List containing the first n Fibonacci numbers
        
    Raises:
        ValueError: If n is negative
        
    Example:
        >>> fib_sequence = fibonacci_generator(8)
        >>> print(fib_sequence)
        [0, 1, 1, 2, 3, 5, 8, 13]
    """
    if n < 0:
        raise ValueError(f"Cannot generate Fibonacci sequence for negative count: {n}")
    
    if n == 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    
    return sequence


def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle.
    
    Uses the mathematical formula À * r² to compute circle area.
    Includes input validation for non-negative radius values.
    
    Args:
        radius: Circle radius (must be non-negative)
        
    Returns:
        float: Circle area
        
    Raises:
        ValueError: If radius is negative
    """
    import math
    
    if radius < 0:
        raise ValueError(f"Circle radius cannot be negative: {radius}")
    
    return math.pi * radius * radius


async def simulate_network_operation(duration_seconds: float = 1.0) -> Dict[str, Any]:
    """Simulate an asynchronous network operation.
    
    Demonstrates async/await patterns with error handling and timeout support.
    Useful for testing async code paths and concurrent operations.
    
    Args:
        duration_seconds: How long to simulate the operation
        
    Returns:
        dict: Simulated response data
    """
    start_time = time.time()
    
    try:
        await asyncio.sleep(duration_seconds)
        
        return {
            "success": True,
            "duration": time.time() - start_time,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "data": "Simulated network response"
        }
    
    except asyncio.CancelledError:
        return {
            "success": False,
            "error": "Operation was cancelled",
            "duration": time.time() - start_time
        }


@contextmanager
def database_transaction(connection: sqlite3.Connection):
    """Context manager for database transactions.
    
    Provides automatic transaction management with rollback on errors.
    Demonstrates context manager patterns for resource management.
    
    Args:
        connection: SQLite database connection
        
    Yields:
        sqlite3.Cursor: Database cursor for operations
        
    Example:
        >>> with database_transaction(conn) as cursor:
        ...     cursor.execute("INSERT INTO users VALUES (?, ?)", (name, email))
    """
    cursor = connection.cursor()
    try:
        yield cursor
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()


# Main Application - Demonstration of comprehensive functionality
async def main() -> None:
    """Main application entry point.
    
    Demonstrates the complete application functionality including:
    - Dependency injection and service initialization
    - Async/await patterns for concurrent operations
    - Comprehensive error handling and logging
    - Data processing and statistical analysis
    - Resource cleanup and graceful shutdown
    """
    print(f"{SystemConstants.APP_NAME} v{SystemConstants.APP_VERSION}")
    print("=" * 50)
    
    # Initialize services with dependency injection
    logger = StructuredLogger(LogLevel.INFO)
    repository = InMemoryUserRepository()
    user_service = UserService(repository, logger)
    
    logger.log(LogLevel.INFO, "Application started", version=SystemConstants.APP_VERSION)
    
    try:
        # Create sample users asynchronously
        logger.log(LogLevel.INFO, "Creating sample users")
        
        users_to_create = [
            ("Alice Johnson", "alice@example.com", 28),
            ("Bob Smith", "bob@example.com", 16),
            ("Carol Brown", "carol@example.com", 35),
            ("David Wilson", "david@example.com", None),
        ]
        
        # Create users concurrently
        user_creation_tasks = [
            user_service.create_user_async(name, email, age)
            for name, email, age in users_to_create
        ]
        
        created_users = await asyncio.gather(*user_creation_tasks, return_exceptions=True)
        
        # Process results and handle any errors
        successful_users = []
        for i, result in enumerate(created_users):
            if isinstance(result, Exception):
                logger.log(
                    LogLevel.ERROR,
                    "Failed to create user",
                    user_data=users_to_create[i],
                    error=str(result)
                )
            else:
                successful_users.append(result)
        
        logger.log(
            LogLevel.INFO,
            "User creation completed",
            successful_count=len(successful_users),
            failed_count=len(created_users) - len(successful_users)
        )
        
        # Display created users
        print(f"\nSuccessfully created {len(successful_users)} users:")
        for user in successful_users:
            print(f"  {user.name} ({user.email}) - Status: {user.status.name}")
        
        # Generate and display statistics
        stats = user_service.get_user_statistics()
        print(f"\nUser Statistics:")
        print(json.dumps(stats, indent=2, default=str))
        
        # Demonstrate mathematical functions
        print(f"\nMathematical Examples:")
        fib_sequence = fibonacci_generator(10)
        print(f"First 10 Fibonacci numbers: {fib_sequence}")
        
        circle_area = calculate_circle_area(5.0)
        print(f"Area of circle with radius 5.0: {circle_area:.2f}")
        
        # Demonstrate async network simulation
        print(f"\nSimulating network operations...")
        network_tasks = [
            simulate_network_operation(0.5),
            simulate_network_operation(1.0),
            simulate_network_operation(0.3)
        ]
        
        network_results = await asyncio.gather(*network_tasks)
        for i, result in enumerate(network_results):
            print(f"  Operation {i+1}: {result['success']} "
                  f"(duration: {result['duration']:.3f}s)")
        
    except KeyboardInterrupt:
        logger.log(LogLevel.WARNING, "Application interrupted by user")
    except Exception as e:
        logger.log(
            LogLevel.CRITICAL,
            "Unhandled application error",
            error=str(e),
            error_type=type(e).__name__
        )
        raise
    
    finally:
        # Cleanup and final logging
        final_stats = user_service.get_user_statistics()
        logger.log(
            LogLevel.INFO,
            "Application shutdown",
            final_user_count=final_stats.get('total_users', 0),
            uptime_seconds=final_stats.get('service_uptime_seconds', 0)
        )
        print(f"\nApplication completed successfully!")


# Module Entry Point
if __name__ == "__main__":
    # Configure logging for the application
    logging.basicConfig(
        level=logging.INFO,
        format=SystemConstants.LOG_FORMAT,
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    # Run the main application
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nApplication interrupted by user")
    except Exception as e:
        logging.critical(f"Fatal application error: {e}")
        raise