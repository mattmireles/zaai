// === source_rust.rs ===
/**
 * ZAAI Environment Test - Rust Language Source File
 * 
 * This Rust source file serves as a comprehensive test artifact for validating
 * the ZAAI system's ability to process, parse, and understand Rust language
 * source code. It demonstrates idiomatic Rust programming patterns while
 * following AI-first documentation principles established in the ZAAI codebase.
 * 
 * Architecture Purpose:
 * This file is referenced by the test domain (domains/test/test.yaml) as
 * part of the environment validation benchmark. It validates the system's
 * capability to handle Rust source files with memory safety, ownership
 * patterns, and modern Rust idioms in the workspace environment.
 * 
 * Cross-file Dependencies:
 * - Referenced by: domains/test/test.yaml (env benchmark)
 * - Used by: Environment test functions that validate Rust file processing
 * - Part of: Multi-language source code validation test suite
 * 
 * Rust Language Features Demonstrated:
 * - Ownership and borrowing system with lifetime management
 * - Pattern matching with match expressions and enums
 * - Error handling with Result types and custom error definitions
 * - Trait system for shared behavior and polymorphism
 * - Memory safety without garbage collection
 * - Zero-cost abstractions and performance optimizations
 * - Generic types and associated types
 * - Struct and impl blocks with method definitions
 * - Module system and visibility controls
 * - Standard library collections and iterators
 * 
 * AI Comprehension Notes:
 * This file contains representative Rust code that demonstrates the language's
 * unique approach to memory safety and systems programming. An AI system
 * should be able to understand Rust's ownership model, the type system's
 * role in preventing memory errors, and the language's emphasis on
 * zero-cost abstractions.
 * 
 * Compilation Requirements:
 * This file is designed as a standalone Rust program that can be compiled
 * and executed using Cargo or rustc with standard Rust tooling.
 */

use std::collections::HashMap;
use std::fmt;
use std::error::Error;
use std::time::{SystemTime, UNIX_EPOCH};

// Constants
const APP_NAME: &str = "Rust Test Application";
const VERSION: &str = "1.0.0";
const MAX_USERS: usize = 1000;

// Custom error type
#[derive(Debug)]
enum AppError {
    UserNotFound(u32),
    InvalidEmail(String),
    RepositoryError(String),
}

impl fmt::Display for AppError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            AppError::UserNotFound(id) => write!(f, "User with ID {} not found", id),
            AppError::InvalidEmail(email) => write!(f, "Invalid email format: {}", email),
            AppError::RepositoryError(msg) => write!(f, "Repository error: {}", msg),
        }
    }
}

impl Error for AppError {}

// Type aliases
type UserId = u32;
type Result<T> = std::result::Result<T, AppError>;

// Enums
#[derive(Debug, Clone, PartialEq)]
enum UserStatus {
    Active,
    Inactive,
    Pending,
}

#[derive(Debug, Clone)]
enum LogLevel {
    Info,
    Warn,
    Error,
    Debug,
}

// Structs
#[derive(Debug, Clone)]
struct UserPreferences {
    theme: String,
    notifications: bool,
    language: String,
}

#[derive(Debug, Clone)]
struct User {
    id: UserId,
    name: String,
    email: String,
    age: Option<u8>,
    status: UserStatus,
    preferences: UserPreferences,
    created_at: u64,
}

impl User {
    fn new(id: UserId, name: String, email: String, age: Option<u8>) -> Result<Self> {
        if !is_valid_email(&email) {
            return Err(AppError::InvalidEmail(email));
        }

        let timestamp = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .unwrap()
            .as_secs();

        Ok(User {
            id,
            name,
            email,
            age,
            status: UserStatus::Active,
            preferences: UserPreferences {
                theme: "light".to_string(),
                notifications: true,
                language: "en".to_string(),
            },
            created_at: timestamp,
        })
    }

    fn is_adult(&self) -> bool {
        self.age.map_or(false, |age| age >= 18)
    }

    fn update_status(&mut self, status: UserStatus) {
        self.status = status;
    }
}

impl fmt::Display for User {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(
            f,
            "User {{ id: {}, name: {}, email: {}, status: {:?} }}",
            self.id, self.name, self.email, self.status
        )
    }
}

// Traits
trait Repository<T> {
    fn save(&mut self, item: T) -> Result<()>;
    fn find_by_id(&self, id: UserId) -> Result<&T>;
    fn find_all(&self) -> Vec<&T>;
    fn delete(&mut self, id: UserId) -> Result<()>;
}

trait Logger {
    fn log(&self, level: LogLevel, message: &str);
    fn info(&self, message: &str) {
        self.log(LogLevel::Info, message);
    }
    fn error(&self, message: &str) {
        self.log(LogLevel::Error, message);
    }
}

// Implementations
struct InMemoryUserRepository {
    users: HashMap<UserId, User>,
    next_id: UserId,
}

impl InMemoryUserRepository {
    fn new() -> Self {
        Self {
            users: HashMap::new(),
            next_id: 1,
        }
    }

    fn create_user(&mut self, name: String, email: String, age: Option<u8>) -> Result<UserId> {
        if self.users.len() >= MAX_USERS {
            return Err(AppError::RepositoryError("Maximum users reached".to_string()));
        }

        let id = self.next_id;
        let user = User::new(id, name, email, age)?;
        self.users.insert(id, user);
        self.next_id += 1;
        Ok(id)
    }
}

impl Repository<User> for InMemoryUserRepository {
    fn save(&mut self, user: User) -> Result<()> {
        self.users.insert(user.id, user);
        Ok(())
    }

    fn find_by_id(&self, id: UserId) -> Result<&User> {
        self.users.get(&id).ok_or(AppError::UserNotFound(id))
    }

    fn find_all(&self) -> Vec<&User> {
        self.users.values().collect()
    }

    fn delete(&mut self, id: UserId) -> Result<()> {
        self.users.remove(&id).ok_or(AppError::UserNotFound(id))?;
        Ok(())
    }
}

struct SimpleLogger;

impl Logger for SimpleLogger {
    fn log(&self, level: LogLevel, message: &str) {
        let timestamp = SystemTime::now()
            .duration_since(UNIX_EPOCH)
            .unwrap()
            .as_secs();
        println!("[{}] {:?}: {}", timestamp, level, message);
    }
}

// Service layer
struct UserService<R: Repository<User>, L: Logger> {
    repository: R,
    logger: L,
}

impl<R: Repository<User>, L: Logger> UserService<R, L> {
    fn new(repository: R, logger: L) -> Self {
        Self { repository, logger }
    }

    fn get_user_stats(&self) -> HashMap<String, u32> {
        let users = self.repository.find_all();
        let mut stats = HashMap::new();
        
        let total = users.len() as u32;
        let adults = users.iter().filter(|u| u.is_adult()).count() as u32;
        let active = users.iter()
            .filter(|u| u.status == UserStatus::Active)
            .count() as u32;

        stats.insert("total".to_string(), total);
        stats.insert("adults".to_string(), adults);
        stats.insert("active".to_string(), active);
        stats.insert("minors".to_string(), total - adults);

        stats
    }
}

// Utility functions
fn is_valid_email(email: &str) -> bool {
    email.contains('@') && email.contains('.')
}

fn fibonacci(n: usize) -> Vec<u64> {
    match n {
        0 => vec![],
        1 => vec![0],
        _ => {
            let mut fib = vec![0, 1];
            for i in 2..n {
                let next = fib[i - 1] + fib[i - 2];
                fib.push(next);
            }
            fib
        }
    }
}

fn calculate_circle_area(radius: f64) -> f64 {
    std::f64::consts::PI * radius * radius
}

// Generic function
fn find_max<T: PartialOrd + Copy>(items: &[T]) -> Option<T> {
    items.iter().max().copied()
}

// Main function
fn main() -> Result<()> {
    println!("{} v{}", APP_NAME, VERSION);
    println!("{}", "=".repeat(30));

    // Initialize dependencies
    let logger = SimpleLogger;
    let mut repository = InMemoryUserRepository::new();
    
    logger.info("Application started");

    // Create sample users
    let user1_id = repository.create_user(
        "Alice Johnson".to_string(),
        "alice@example.com".to_string(),
        Some(28),
    )?;

    let user2_id = repository.create_user(
        "Bob Smith".to_string(),
        "bob@example.com".to_string(),
        Some(16),
    )?;

    let user3_id = repository.create_user(
        "Charlie Brown".to_string(),
        "charlie@example.com".to_string(),
        None,
    )?;

    logger.info(&format!("Created {} users", 3));

    // Display users
    println!("\nCreated Users:");
    for &id in &[user1_id, user2_id, user3_id] {
        match repository.find_by_id(id) {
            Ok(user) => println!("  {}", user),
            Err(e) => logger.error(&format!("Error finding user {}: {}", id, e)),
        }
    }

    // Service layer example
    let service = UserService::new(repository, logger);
    
    // Get statistics
    let stats = service.get_user_stats();
    println!("\nUser Statistics:");
    for (key, value) in &stats {
        println!("  {}: {}", key, value);
    }

    // Math examples
    println!("\nMath Examples:");
    let circle_area = calculate_circle_area(5.0);
    println!("Circle area (radius 5.0): {:.2}", circle_area);

    let fib_numbers = fibonacci(10);
    println!("First 10 Fibonacci numbers: {:?}", fib_numbers);

    let numbers = vec![1, 5, 3, 9, 2, 8];
    if let Some(max_num) = find_max(&numbers) {
        println!("Maximum number in {:?}: {}", numbers, max_num);
    }

    // Demonstrate error handling
    match service.repository.find_by_id(999) {
        Ok(user) => println!("Found user: {}", user),
        Err(e) => println!("Expected error: {}", e),
    }

    service.logger.info("Application completed successfully");
    Ok(())
}