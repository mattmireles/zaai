// === source_js.js ===
/**
 * JavaScript Test File - Modern ES6+ Features
 * Demonstrates various JavaScript concepts and patterns
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