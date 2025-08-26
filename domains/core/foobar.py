"""Workspace Reference Classes for ZAAI Multi-file Python Project Benchmark

This module serves as a reference implementation for the multi-file Python project
benchmark defined in domains/core/core.yaml. It provides sample classes that are
imported and used by benchmark test functions to validate the AI's ability to work
with existing workspace files and handle cross-file dependencies.

Architecture Overview:
This file is referenced by the "foobar" benchmark in core.yaml through the 
references section, specifically mapped to the workspace as "foobar.py". The
benchmark test functions in core.yaml import this module to instantiate and
interact with the defined classes.

Usage Pattern:
1. Benchmark system maps this file into the workspace execution environment
2. Test functions import classes using: `from main import create_foo_bar_baz`  
3. Test functions call do_something() methods to validate expected return values
4. Classes return specific strings containing their class names for verification

Cross-file Dependencies:
- Referenced by: domains/core/core.yaml (foobar benchmark)
- Used by: Test functions in the foobar benchmark specification
- Expected by: create_foo_bar_baz() function in main.py (implemented by AI)

This design demonstrates the AI's ability to understand workspace file structure,
import existing modules, and build upon provided foundation code.
"""

class ProcessingConstants:
    """Constants for consistent string processing and class identification.
    
    These constants ensure that the class methods return predictable strings
    that can be validated by test functions. Using named constants follows
    the AI-first documentation philosophy of making all values explicit.
    """
    FOO_ACTION_RESULT = "Foo did something successfully"
    BAR_ACTION_RESULT = "Bar performed its action"
    BAZ_ACTION_RESULT = "Baz executed its method"


class Foo:
    """Sample workspace class representing the Foo entity.
    
    This class serves as a reference implementation for multi-file Python projects.
    It demonstrates basic class structure and method implementation that benchmark
    test functions can validate against.
    
    The class is intentionally simple to focus on cross-file dependency management
    rather than complex functionality. Its primary purpose is to validate that
    the AI can import and instantiate workspace classes correctly.
    """
    
    def __init__(self):
        """Initialize the Foo instance.
        
        No complex initialization is required as this class serves as a simple
        reference implementation for testing workspace file integration.
        """
        pass

    def do_something(self) -> str:
        """Execute the primary action for this Foo instance.
        
        This method implements the standard interface expected by benchmark test
        functions. The return value is specifically chosen to contain the class
        name for verification purposes.
        
        Returns:
            str: A success message containing the class name "Foo" for test validation.
            
        Example:
            >>> foo = Foo()
            >>> result = foo.do_something()
            >>> assert "Foo" in result
            >>> assert result == "Foo did something successfully"
        """
        return ProcessingConstants.FOO_ACTION_RESULT


class Bar:
    """Sample workspace class representing the Bar entity.
    
    This class provides a second reference implementation to demonstrate that
    the AI can work with multiple classes from the same workspace file. It
    follows the same interface pattern as Foo for consistency.
    
    The class serves as part of the multi-file project structure validation,
    ensuring that the AI can handle multiple class definitions and distinguish
    between their behaviors.
    """
    
    def __init__(self):
        """Initialize the Bar instance.
        
        Similar to Foo, this class requires no complex initialization as its
        primary purpose is to validate workspace integration capabilities.
        """
        pass

    def do_something(self) -> str:
        """Execute the primary action for this Bar instance.
        
        This method provides the same interface as Foo.do_something() but returns
        a Bar-specific message. This allows test functions to verify that the
        correct class instance is being used.
        
        Returns:
            str: A success message containing the class name "Bar" for test validation.
            
        Example:
            >>> bar = Bar()
            >>> result = bar.do_something()
            >>> assert "Bar" in result
            >>> assert result == "Bar performed its action"
        """
        return ProcessingConstants.BAR_ACTION_RESULT


class Baz:
    """Sample workspace class representing the Baz entity.
    
    This class completes the trio of reference implementations, providing a third
    distinct class for comprehensive multi-file project testing. It maintains
    the same interface pattern for consistency while providing unique behavior.
    
    The inclusion of three classes allows benchmark tests to verify that the AI
    can handle multiple class instantiations and method calls within a single
    workspace file context.
    """
    
    def __init__(self):
        """Initialize the Baz instance.
        
        Consistent with the other classes, this provides minimal initialization
        as the focus is on workspace integration rather than complex functionality.
        """
        pass

    def do_something(self) -> str:
        """Execute the primary action for this Baz instance.
        
        This method completes the standard interface implementation, providing
        a Baz-specific return value that can be validated by benchmark test
        functions to confirm correct class usage.
        
        Returns:
            str: A success message containing the class name "Baz" for test validation.
            
        Example:
            >>> baz = Baz()
            >>> result = baz.do_something()
            >>> assert "Baz" in result
            >>> assert result == "Baz executed its method"
        """
        return ProcessingConstants.BAZ_ACTION_RESULT