// === source_js.js ===
/**
 * ZAAI Environment Test - JavaScript Source File
 * 
 * This JavaScript source file serves as a comprehensive test artifact for
 * validating the ZAAI system's ability to process, parse, and understand
 * modern JavaScript (ES6+) source code. It demonstrates contemporary
 * JavaScript development patterns while following AI-first documentation
 * principles established in the ZAAI codebase.
 * 
 * Architecture Purpose:
 * This file is referenced by the test domain (domains/test/test.yaml) as
 * part of the environment validation benchmark. It validates the system's
 * capability to handle JavaScript files with modern syntax and patterns
 * in the workspace environment.
 * 
 * Cross-file Dependencies:
 * - Referenced by: domains/test/test.yaml (env benchmark)  
 * - Used by: Environment test functions that validate JavaScript file processing
 * - Part of: Multi-language source code validation test suite
 * 
 * JavaScript Features Demonstrated:
 * - ES6+ class syntax and inheritance patterns
 * - Modern variable declarations (const, let)
 * - Arrow functions and functional programming patterns
 * - Async/await and Promise-based asynchronous programming
 * - Destructuring assignment and spread operators
 * - Template literals and string interpolation
 * - Array methods (map, filter, reduce) and functional approaches
 * - Module exports (CommonJS and ES modules compatibility)
 * - Error handling and exception management
 * 
 * AI Comprehension Notes:
 * This file contains representative modern JavaScript code that an AI
 * system should be able to analyze, understand, and potentially modify.
 * It includes current JavaScript idioms, async patterns, and object-oriented
 * programming approaches typical in contemporary JavaScript development.
 * 
 * Node.js Compatibility:
 * The code is designed to run in both browser and Node.js environments,
 * demonstrating cross-platform JavaScript development practices.
 */

// Constants and variables
const APP_NAME = 'JavaScript Test Application';
const VERSION = '1.0.0';

let globalCounter = 0;

// ES6 Classes
class TaskManager {
    constructor(name) {
        this.name = name;
        this.tasks = [];
        this.completedCount = 0;
        console.log(`TaskManager '${name}' initialized`);
    }
    
    addTask(description, priority = 'medium') {
        const task = {
            id: Date.now(),
            description,
            priority,
            completed: false,
            createdAt: new Date()
        };
        this.tasks.push(task);
        return task;
    }
    
    completeTask(taskId) {
        const task = this.tasks.find(t => t.id === taskId);
        if (task && !task.completed) {
            task.completed = true;
            task.completedAt = new Date();
            this.completedCount++;
            return true;
        }
        return false;
    }
    
    getTasks(filter = 'all') {
        switch (filter) {
            case 'completed':
                return this.tasks.filter(task => task.completed);
            case 'pending':
                return this.tasks.filter(task => !task.completed);
            default:
                return [...this.tasks];
        }
    }
    
    getStats() {
        return {
            total: this.tasks.length,
            completed: this.completedCount,
            pending: this.tasks.length - this.completedCount
        };
    }
}

// Utility functions
const utils = {
    // Arrow function with destructuring
    formatTask: ({ description, priority, completed }) => 
        `[${priority.toUpperCase()}] ${description} ${completed ? '✓' : '○'}`,
    
    // Async function
    async delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    },
    
    // Higher-order function
    createLogger: (prefix) => (message) => {
        console.log(`[${prefix}] ${new Date().toISOString()}: ${message}`);
    },
    
    // Function with default parameters and rest operator
    calculateAverage: (...numbers) => {
        if (numbers.length === 0) return 0;
        const sum = numbers.reduce((acc, num) => acc + num, 0);
        return sum / numbers.length;
    }
};

// Main execution function
async function main() {
    console.log(`${APP_NAME} v${VERSION}`);
    console.log('='.repeat(40));
    
    // Create task manager
    const taskManager = new TaskManager('Daily Tasks');
    const logger = utils.createLogger('MAIN');
    
    // Add some tasks
    const task1 = taskManager.addTask('Learn JavaScript ES6+', 'high');
    const task2 = taskManager.addTask('Write unit tests', 'medium');
    const task3 = taskManager.addTask('Deploy application', 'low');
    
    logger('Tasks created');
    
    // Complete a task
    taskManager.completeTask(task1.id);
    logger('Task completed');
    
    // Display tasks
    console.log('\nAll Tasks:');
    taskManager.getTasks().forEach(task => {
        console.log('  ' + utils.formatTask(task));
    });
    
    // Show statistics
    const stats = taskManager.getStats();
    console.log(`\nStats: ${stats.completed}/${stats.total} completed`);
    
    // Demonstrate async/await
    console.log('\nWaiting 1 second...');
    await utils.delay(1000);
    console.log('Done!');
    
    // Array methods demonstration
    const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    const evenNumbers = numbers.filter(n => n % 2 === 0);
    const squares = numbers.map(n => n * n);
    const sum = numbers.reduce((acc, n) => acc + n, 0);
    
    console.log(`\nArray operations:`);
    console.log(`Even numbers: ${evenNumbers.join(', ')}`);
    console.log(`Squares: ${squares.join(', ')}`);
    console.log(`Sum: ${sum}`);
    console.log(`Average: ${utils.calculateAverage(...numbers)}`);
}

// Module exports (CommonJS style)
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { TaskManager, utils };
}

// Run main function if this is the entry point
if (require.main === module) {
    main().catch(console.error);
}