#include <stdio.h>
#include <string.h>

struct Book { int sn; char title[100], author[50]; int copies, available; };
struct Borrower { int id; char name[50]; int books_borrowed; };
struct Transaction { int book_sn, borrower_id; char type[10], date[20]; };

struct Library {
    struct Book books[100];
    struct Borrower borrowers[50];
    struct Transaction transactions[200];
    int total_books, total_borrowers, total_transactions;
} library;

void init() {
    library.total_books = library.total_borrowers = library.total_transactions = 0;
}

void save() {
    FILE *f = fopen("library.dat", "wb");
    if(f) { fwrite(&library, sizeof(library), 1, f); fclose(f); }
}

void load() {
    FILE *f = fopen("library.dat", "rb");
    if(f) { fread(&library, sizeof(library), 1, f); fclose(f); }
}

void addBook() {
    if(library.total_books >= 100) { printf("Book limit reached!\n"); return; }
    struct Book b;
    printf("Enter SN, Title, Author, Copies: ");
    scanf("%d %s %s %d", &b.sn, b.title, b.author, &b.copies);
    b.available = b.copies;
    library.books[library.total_books++] = b;
    save();
}

void addBorrower() {
    if(library.total_borrowers >= 50) { printf("Borrower limit reached!\n"); return; }
    struct Borrower br;
    printf("Enter ID, Name: ");
    scanf("%d %s", &br.id, br.name);
    br.books_borrowed = 0;
    library.borrowers[library.total_borrowers++] = br;
    save();
}

void issueBook() {
    int sn, id;
    printf("Enter Book SN and Borrower ID: ");
    scanf("%d %d", &sn, &id);
    
    for(int i=0; i<library.total_books; i++) {
        if(library.books[i].sn == sn && library.books[i].available > 0) {
            for(int j=0; j<library.total_borrowers; j++) {
                if(library.borrowers[j].id == id) {
                    library.books[i].available--;
                    library.borrowers[j].books_borrowed++;
                    
                    struct Transaction t;
                    t.book_sn = sn;
                    t.borrower_id = id;
                    strcpy(t.type, "issue");
                    strcpy(t.date, "today");
                    library.transactions[library.total_transactions++] = t;
                    
                    printf("Book issued!\n");
                    save();
                    return;
                }
            }
        }
    }
    printf("Operation failed!\n");
}

void returnBook() {
    int sn, id;
    printf("Enter Book SN and Borrower ID: ");
    scanf("%d %d", &sn, &id);
    
    for(int i=0; i<library.total_books; i++) {
        if(library.books[i].sn == sn) {
            for(int j=0; j<library.total_borrowers; j++) {
                if(library.borrowers[j].id == id && library.borrowers[j].books_borrowed > 0) {
                    library.books[i].available++;
                    library.borrowers[j].books_borrowed--;
                    
                    struct Transaction t;
                    t.book_sn = sn;
                    t.borrower_id = id;
                    strcpy(t.type, "return");
                    strcpy(t.date, "today");
                    library.transactions[library.total_transactions++] = t;
                    
                    printf("Book returned!\n");
                    save();
                    return;
                }
            }
        }
    }
    printf("Operation failed!\n");
}

void showBooks() {
    printf("\nBooks:\nSN\tTitle\tAvailable\n");
    for(int i=0; i<library.total_books; i++)
        printf("%d\t%s\t%d/%d\n", library.books[i].sn, library.books[i].title, 
              library.books[i].available, library.books[i].copies);
}

void showBorrowers() {
    printf("\nBorrowers:\nID\tName\tBooks\n");
    for(int i=0; i<library.total_borrowers; i++)
        printf("%d\t%s\t%d\n", library.borrowers[i].id, 
              library.borrowers[i].name, library.borrowers[i].books_borrowed);
}

int main() {
    init();
    load();
    
    int choice;
    do {
        printf("\n1. Add Book\n2. Add Borrower\n3. Issue Book\n4. Return Book\n5. Show Books\n6. Show Borrowers\n0. Exit\nChoice: ");
        scanf("%d", &choice);
        
        switch(choice) {
            case 1: addBook(); break;
            case 2: addBorrower(); break;
            case 3: issueBook(); break;
            case 4: returnBook(); break;
            case 5: showBooks(); break;
            case 6: showBorrowers(); break;
            case 0: save(); break;
            default: printf("Invalid choice!\n");
        }
    } while(choice != 0);
    
    return 0;
}