// === source_ts.ts ===
/**
 * ZAAI Environment Test - TypeScript Source File
 * 
 * This TypeScript source file serves as a comprehensive test artifact for
 * validating the ZAAI system's ability to process, parse, and understand
 * TypeScript source code with advanced type system features. It demonstrates
 * modern TypeScript development patterns while following AI-first documentation
 * principles established in the ZAAI codebase.
 * 
 * Architecture Purpose:
 * This file is referenced by the test domain (domains/test/test.yaml) as
 * part of the environment validation benchmark. It validates the system's
 * capability to handle TypeScript files with complex type definitions,
 * generics, and advanced language features in the workspace environment.
 * 
 * Cross-file Dependencies:
 * - Referenced by: domains/test/test.yaml (env benchmark)
 * - Used by: Environment test functions that validate TypeScript file processing
 * - Part of: Multi-language source code validation test suite
 * 
 * TypeScript Features Demonstrated:
 * - Interface definitions and type contracts
 * - Generic types and constraint-based programming
 * - Union types and literal type definitions
 * - Optional properties and nullable types
 * - Enum definitions and string literal unions
 * - Advanced utility types (Pick, Omit, Partial)
 * - Type guards and type narrowing
 * - Namespace organization and module systems
 * - Dependency injection patterns with typed interfaces
 * - Comprehensive error handling with typed exceptions
 * 
 * AI Comprehension Notes:
 * This file contains representative TypeScript code that demonstrates
 * the language's type system capabilities. An AI system should be able
 * to understand the type relationships, interface contracts, and
 * compile-time safety guarantees provided by TypeScript's static typing.
 * 
 * Compilation Target:
 * The code is designed to compile to ES2020+ JavaScript with full
 * type checking enabled, demonstrating production-ready TypeScript
 * development practices.
 */

// Type definitions
interface User {
    readonly id: number;
    name: string;
    email: string;
    age?: number;
    preferences: UserPreferences;
}

interface UserPreferences {
    theme: 'light' | 'dark';
    notifications: boolean;
    language: string;
}

type Status = 'active' | 'inactive' | 'pending';
type UserRole = 'admin' | 'user' | 'moderator';

// Generic interface
interface Repository<T> {
    findById(id: number): T | null;
    findAll(): T[];
    save(entity: T): T;
    delete(id: number): boolean;
}

// Enum
enum LogLevel {
    DEBUG = 0,
    INFO = 1,
    WARN = 2,
    ERROR = 3
}

// Generic class
class UserRepository implements Repository<User> {
    private users: Map<number, User> = new Map();
    private nextId: number = 1;

    findById(id: number): User | null {
        return this.users.get(id) || null;
    }

    findAll(): User[] {
        return Array.from(this.users.values());
    }

    save(user: Omit<User, 'id'>): User {
        const newUser: User = {
            ...user,
            id: this.nextId++
        };
        this.users.set(newUser.id, newUser);
        return newUser;
    }

    delete(id: number): boolean {
        return this.users.delete(id);
    }

    findByEmail(email: string): User | null {
        for (const user of this.users.values()) {
            if (user.email === email) {
                return user;
            }
        }
        return null;
    }
}

// Service class with dependency injection
class UserService {
    constructor(
        private userRepository: UserRepository,
        private logger: Logger
    ) {}

    async createUser(userData: Omit<User, 'id'>): Promise<User> {
        this.logger.log(LogLevel.INFO, `Creating user: ${userData.email}`);
        
        // Validation
        if (!this.isValidEmail(userData.email)) {
            throw new Error('Invalid email format');
        }

        // Check if user already exists
        const existingUser = this.userRepository.findByEmail(userData.email);
        if (existingUser) {
            throw new Error('User already exists');
        }

        const user = this.userRepository.save(userData);
        this.logger.log(LogLevel.INFO, `User created with ID: ${user.id}`);
        return user;
    }

    async getUsersByStatus(status: Status): Promise<User[]> {
        // This is a simplified example - in reality, status might be stored separately
        const allUsers = this.userRepository.findAll();
        this.logger.log(LogLevel.DEBUG, `Found ${allUsers.length} total users`);
        return allUsers; // Simplified for demo
    }

    private isValidEmail(email: string): boolean {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
}

// Logger class
class Logger {
    log(level: LogLevel, message: string): void {
        const timestamp = new Date().toISOString();
        const levelName = LogLevel[level];
        console.log(`[${timestamp}] ${levelName}: ${message}`);
    }

    debug(message: string): void {
        this.log(LogLevel.DEBUG, message);
    }

    info(message: string): void {
        this.log(LogLevel.INFO, message);
    }

    warn(message: string): void {
        this.log(LogLevel.WARN, message);
    }

    error(message: string): void {
        this.log(LogLevel.ERROR, message);
    }
}

// Utility functions with advanced types
namespace Utils {
    export function pick<T, K extends keyof T>(obj: T, keys: K[]): Pick<T, K> {
        const result: any = {};
        keys.forEach(key => {
            if (key in obj) {
                result[key] = obj[key];
            }
        });
        return result;
    }

    export function omit<T, K extends keyof T>(obj: T, keys: K[]): Omit<T, K> {
        const result: any = { ...obj };
        keys.forEach(key => {
            delete result[key];
        });
        return result;
    }

    export function isNotNull<T>(value: T | null | undefined): value is T {
        return value !== null && value !== undefined;
    }
}

// Main application
async function main(): Promise<void> {
    console.log('TypeScript Test Application');
    console.log('===========================');

    // Initialize services
    const logger = new Logger();
    const userRepository = new UserRepository();
    const userService = new UserService(userRepository, logger);

    try {
        // Create sample users
        const user1 = await userService.createUser({
            name: 'Alice Johnson',
            email: 'alice@example.com',
            age: 28,
            preferences: {
                theme: 'dark',
                notifications: true,
                language: 'en'
            }
        });

        const user2 = await userService.createUser({
            name: 'Bob Smith',
            email: 'bob@example.com',
            preferences: {
                theme: 'light',
                notifications: false,
                language: 'es'
            }
        });

        logger.info(`Created users: ${user1.name}, ${user2.name}`);

        // Demonstrate utility functions
        const userSummary = Utils.pick(user1, ['id', 'name', 'email']);
        console.log('User summary:', userSummary);

        const allUsers = userRepository.findAll();
        const validUsers = allUsers.filter(Utils.isNotNull);
        logger.info(`Found ${validUsers.length} valid users`);

    } catch (error) {
        logger.error(`Application error: ${error.message}`);
    }
}

// Run the application
if (require.main === module) {
    main().catch(console.error);
}