#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CUSTOMERS 100
#define MAX_NAME_LENGTH 50
#define DATA_FILE "bank_data.dat"


struct Customer {
    int accountNumber;
    char name[MAX_NAME_LENGTH];
    double balance;
    char password[20];
};


struct Bank {
    struct Customer customers[MAX_CUSTOMERS];
    int totalCustomers;
};


struct Bank myBank;


void initializeBank();
void createAccount();
void deposit();
void withdraw();
void checkBalance();
void displayAllAccounts();
void transferMoney();
int findCustomer(int accountNumber);
void saveToFile();
int loadFromFile();
void adminMenu();
int authenticateCustomer(int accountNumber);

int main() {
    initializeBank();
    
    if (!loadFromFile()) {
        printf("Starting with fresh data.\n");
    }

    adminMenu();
    
    return 0;
}

void initializeBank() {
    myBank.totalCustomers = 0;
    memset(myBank.customers, 0, sizeof(myBank.customers));
}

void adminMenu() {
    int choice;
    do {
        printf("\n===== Banking System Admin Menu =====\n");
        printf("1. Create New Account\n");
        printf("2. Deposit Money\n");
        printf("3. Withdraw Money\n");
        printf("4. Check Balance\n");
        printf("5. Display All Accounts\n");
        printf("6. Transfer Money\n");
        printf("7. Save Data\n");
        printf("8. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        
        switch(choice) {
            case 1: createAccount(); break;
            case 2: deposit(); break;
            case 3: withdraw(); break;
            case 4: checkBalance(); break;
            case 5: displayAllAccounts(); break;
            case 6: transferMoney(); break;
            case 7: saveToFile(); break;
            case 8: 
                saveToFile();
                printf("Thank you for using our banking system!\n");
                break;
            default: printf("Invalid choice. Please try again.\n");
        }
    } while(choice != 8);
}

void createAccount() {
    if(myBank.totalCustomers >= MAX_CUSTOMERS) {
        printf("Bank capacity reached. Cannot create more accounts.\n");
        return;
    }
    
    struct Customer newCustomer;
    
    printf("\nEnter account number: ");
    scanf("%d", &newCustomer.accountNumber);
    
    if(findCustomer(newCustomer.accountNumber) != -1) {
        printf("Account number already exists!\n");
        return;
    }
    
    printf("Enter customer name: ");
    scanf(" %[^\n]", newCustomer.name);
    
    printf("Enter initial deposit: ");
    scanf("%lf", &newCustomer.balance);
    
    if(newCustomer.balance < 0) {
        printf("Invalid amount. Balance cannot be negative.\n");
        return;
    }
    
    printf("Set account password: ");
    scanf("%s", newCustomer.password);
    
    myBank.customers[myBank.totalCustomers] = newCustomer;
    myBank.totalCustomers++;
    
    printf("Account created successfully!\n");
    printf("Account Number: %d\n", newCustomer.accountNumber);
    
   
    saveToFile();
}

void deposit() {
    int accountNumber;
    double amount;
    
    printf("\nEnter account number: ");
    scanf("%d", &accountNumber);
    
    int index = findCustomer(accountNumber);
    if(index == -1) {
        printf("Account not found!\n");
        return;
    }
    
    printf("Enter amount to deposit: ");
    scanf("%lf", &amount);
    
    if(amount <= 0) {
        printf("Invalid amount. Please enter a positive value.\n");
        return;
    }
    
    myBank.customers[index].balance += amount;
    printf("Deposit successful. New balance: %.2lf\n", myBank.customers[index].balance);
    
    
    saveToFile();
}

void withdraw() {
    int accountNumber;
    double amount;
    
    printf("\nEnter account number: ");
    scanf("%d", &accountNumber);
    
    int index = findCustomer(accountNumber);
    if(index == -1) {
        printf("Account not found!\n");
        return;
    }
    
    if (!authenticateCustomer(accountNumber)) {
        return;
    }
    
    printf("Enter amount to withdraw: ");
    scanf("%lf", &amount);
    
    if(amount <= 0) {
        printf("Invalid amount. Please enter a positive value.\n");
        return;
    }
    
    if(myBank.customers[index].balance < amount) {
        printf("Insufficient balance!\n");
        return;
    }
    
    myBank.customers[index].balance -= amount;
    printf("Withdrawal successful. New balance: %.2lf\n", myBank.customers[index].balance);
    
   
    saveToFile();
}

int authenticateCustomer(int accountNumber) {
    int index = findCustomer(accountNumber);
    if (index == -1) return 0;
    
    char password[20];
    printf("Enter account password: ");
    scanf("%s", password);
    
    if(strcmp(password, myBank.customers[index].password) != 0) {
        printf("Incorrect password!\n");
        return 0;
    }
    return 1;
}

void checkBalance() {
    int accountNumber;
    
    printf("\nEnter account number: ");
    scanf("%d", &accountNumber);
    
    int index = findCustomer(accountNumber);
    if(index == -1) {
        printf("Account not found!\n");
        return;
    }
    
    if (!authenticateCustomer(accountNumber)) {
        return;
    }
    
    printf("Account Holder: %s\n", myBank.customers[index].name);
    printf("Account Balance: %.2lf\n", myBank.customers[index].balance);
}

void displayAllAccounts() {
    if(myBank.totalCustomers == 0) {
        printf("No accounts found!\n");
        return;
    }
    
  
    printf("Account No.\tName\t\tBalance\n\n");
    
    
    for(int i = 0; i < myBank.totalCustomers; i++) {
        printf("%d\t\t%s\t\t%.2lf\n", 
               myBank.customers[i].accountNumber,
               myBank.customers[i].name,
               myBank.customers[i].balance);
    }
}

void transferMoney() {
    int fromAccount, toAccount;
    double amount;
    
    printf("\nEnter your account number: ");
    scanf("%d", &fromAccount);
    
    int fromIndex = findCustomer(fromAccount);
    if(fromIndex == -1) {
        printf("Your account not found!\n");
        return;
    }
    
    if (!authenticateCustomer(fromAccount)) {
        return;
    }
    
    printf("Enter recipient account number: ");
    scanf("%d", &toAccount);
    
    int toIndex = findCustomer(toAccount);
    if(toIndex == -1) {
        printf("Recipient account not found!\n");
        return;
    }
    
    printf("Enter amount to transfer: ");
    scanf("%lf", &amount);
    
    if(amount <= 0) {
        printf("Invalid amount. Please enter a positive value.\n");
        return;
    }
    
    if(myBank.customers[fromIndex].balance < amount) {
        printf("Insufficient balance!\n");
        return;
    }
    
    myBank.customers[fromIndex].balance -= amount;
    myBank.customers[toIndex].balance += amount;
    
    printf("Transfer successful!\n");
    printf("Your new balance: %.2lf\n", myBank.customers[fromIndex].balance);
    
   
    saveToFile();
}

int findCustomer(int accountNumber) {
    for(int i = 0; i < myBank.totalCustomers; i++) {
        if(myBank.customers[i].accountNumber == accountNumber) {
            return i;
        }
    }
    return -1;
}

void saveToFile() {
    FILE *file = fopen(DATA_FILE, "wb");
    if(file == NULL) {
        printf("Error saving data to file!\n");
        return;
    }
  
    if (fwrite(&myBank, sizeof(struct Bank), 1, file) != 1) {
        printf("Error writing data to file!\n");
    } else {
        printf("Data saved successfully to %s\n", DATA_FILE);
    }
    
    fclose(file);
}

int loadFromFile() {
    FILE *file = fopen(DATA_FILE, "rb");
    if(file == NULL) {
        return 0; 
    }
    
   
    if (fread(&myBank, sizeof(struct Bank), 1, file) != 1) {
        fclose(file);
        return 0; 
    }
    
    fclose(file);
    printf("Data loaded successfully from %s\n", DATA_FILE);
    printf("Total customers: %d\n", myBank.totalCustomers);
    return 1;
}