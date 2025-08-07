// === source_go.go ===
package main

import (
    "encoding/json"
    "fmt"
    "log"
    "math"
    "sort"
    "strconv"
    "strings"
    "time"
)

// Constants
const (
    AppName    = "Go Test Application"
    Version    = "1.0.0"
    MaxRetries = 3
)

// Custom types
type UserID int
type Status string

// Enums using constants
const (
    StatusActive   Status = "active"
    StatusInactive Status = "inactive"
    StatusPending  Status = "pending"
)

// Structs
type User struct {
    ID          UserID    `json:"id"`
    Name        string    `json:"name"`
    Email       string    `json:"email"`
    Age         *int      `json:"age,omitempty"`
    Status      Status    `json:"status"`
    CreatedAt   time.Time `json:"created_at"`
    Preferences UserPrefs `json:"preferences"`
}

type UserPrefs struct {
    Theme         string `json:"theme"`
    Notifications bool   `json:"notifications"`
    Language      string `json:"language"`
}

// Interfaces
type Repository interface {
    Save(user *User) error
    FindByID(id UserID) (*User, error)
    FindAll() ([]*User, error)
    Delete(id UserID) error
}

type Logger interface {
    Info(msg string)
    Error(msg string)
    Debug(msg string)
}

// Implementations
type InMemoryRepository struct {
    users  map[UserID]*User
    nextID UserID
}

func NewInMemoryRepository() *InMemoryRepository {
    return &InMemoryRepository{
        users:  make(map[UserID]*User),
        nextID: 1,
    }
}

func (r *InMemoryRepository) Save(user *User) error {
    if user.ID == 0 {
        user.ID = r.nextID
        r.nextID++
    }
    user.CreatedAt = time.Now()
    r.users[user.ID] = user
    return nil
}

func (r *InMemoryRepository) FindByID(id UserID) (*User, error) {
    user, exists := r.users[id]
    if !exists {
        return nil, fmt.Errorf("user with ID %d not found", id)
    }
    return user, nil
}

func (r *InMemoryRepository) FindAll() ([]*User, error) {
    users := make([]*User, 0, len(r.users))
    for _, user := range r.users {
        users = append(users, user)
    }
    return users, nil
}

func (r *InMemoryRepository) Delete(id UserID) error {
    if _, exists := r.users[id]; !exists {
        return fmt.Errorf("user with ID %d not found", id)
    }
    delete(r.users, id)
    return nil
}

// Simple logger implementation
type SimpleLogger struct{}

func (l *SimpleLogger) Info(msg string) {
    log.Printf("[INFO] %s", msg)
}

func (l *SimpleLogger) Error(msg string) {
    log.Printf("[ERROR] %s", msg)
}

func (l *SimpleLogger) Debug(msg string) {
    log.Printf("[DEBUG] %s", msg)
}

// Service layer
type UserService struct {
    repo   Repository
    logger Logger
}

func NewUserService(repo Repository, logger Logger) *UserService {
    return &UserService{
        repo:   repo,
        logger: logger,
    }
}

func (s *UserService) CreateUser(name, email string, age *int) (*User, error) {
    s.logger.Info(fmt.Sprintf("Creating user: %s", email))
    
    if !isValidEmail(email) {
        return nil, fmt.Errorf("invalid email format: %s", email)
    }
    
    user := &User{
        Name:   name,
        Email:  email,
        Age:    age,
        Status: StatusActive,
        Preferences: UserPrefs{
            Theme:         "light",
            Notifications: true,
            Language:      "en",
        },
    }
    
    if err := s.repo.Save(user); err != nil {
        s.logger.Error(fmt.Sprintf("Failed to save user: %v", err))
        return nil, err
    }
    
    s.logger.Info(fmt.Sprintf("User created with ID: %d", user.ID))
    return user, nil
}

func (s *UserService) GetUserStats() (map[string]interface{}, error) {
    users, err := s.repo.FindAll()
    if err != nil {
        return nil, err
    }
    
    stats := map[string]interface{}{
        "total": len(users),
        "by_status": make(map[Status]int),
        "average_age": 0.0,
    }
    
    statusCounts := make(map[Status]int)
    ageSum := 0
    ageCount := 0
    
    for _, user := range users {
        statusCounts[user.Status]++
        if user.Age != nil {
            ageSum += *user.Age
            ageCount++
        }
    }
    
    stats["by_status"] = statusCounts
    if ageCount > 0 {
        stats["average_age"] = float64(ageSum) / float64(ageCount)
    }
    
    return stats, nil
}

// Utility functions
func isValidEmail(email string) bool {
    return strings.Contains(email, "@") && strings.Contains(email, ".")
}

func intPtr(i int) *int {
    return &i
}

// Math utilities
func calculateCircleArea(radius float64) float64 {
    return math.Pi * radius * radius
}

func fibonacci(n int) []int {
    if n <= 0 {
        return []int{}
    }
    if n == 1 {
        return []int{0}
    }
    
    fib := make([]int, n)
    fib[0], fib[1] = 0, 1
    
    for i := 2; i < n; i++ {
        fib[i] = fib[i-1] + fib[i-2]
    }
    
    return fib
}

// Goroutine example
func processNumbers(numbers []int, results chan<- int) {
    sum := 0
    for _, num := range numbers {
        sum += num * num // Square each number
    }
    results <- sum
}

func main() {
    fmt.Printf("%s v%s\n", AppName, Version)
    fmt.Println(strings.Repeat("=", 30))
    
    // Initialize dependencies
    logger := &SimpleLogger{}
    repo := NewInMemoryRepository()
    userService := NewUserService(repo, logger)
    
    // Create sample users
    user1, err := userService.CreateUser("Alice Johnson", "alice@example.com", intPtr(28))
    if err != nil {
        logger.Error(fmt.Sprintf("Failed to create user: %v", err))
        return
    }
    
    user2, err := userService.CreateUser("Bob Smith", "bob@example.com", nil)
    if err != nil {
        logger.Error(fmt.Sprintf("Failed to create user: %v", err))
        return
    }
    
    // Display users as JSON
    fmt.Println("\nCreated Users:")
    for _, user := range []*User{user1, user2} {
        userJSON, _ := json.MarshalIndent(user, "", "  ")
        fmt.Printf("%s\n", userJSON)
    }
    
    // Get and display statistics
    stats, err := userService.GetUserStats()
    if err != nil {
        logger.Error(fmt.Sprintf("Failed to get stats: %v", err))
        return
    }
    
    fmt.Println("\nUser Statistics:")
    statsJSON, _ := json.MarshalIndent(stats, "", "  ")
    fmt.Printf("%s\n", statsJSON)
    
    // Math examples
    fmt.Printf("\nMath Examples:\n")
    fmt.Printf("Circle area (radius 5): %.2f\n", calculateCircleArea(5.0))
    
    fibNumbers := fibonacci(10)
    fmt.Printf("First 10 Fibonacci numbers: %v\n", fibNumbers)
    
    // Goroutine example
    numbers := []int{1, 2, 3, 4, 5}
    results := make(chan int, 1)
    go processNumbers(numbers, results)
    
    squareSum := <-results
    fmt.Printf("Sum of squares of %v: %d\n", numbers, squareSum)
    
    logger.Info("Application completed successfully")
}