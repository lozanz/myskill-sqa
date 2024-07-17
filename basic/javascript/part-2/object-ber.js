let person = {
    firstName: "John",
    lastName: "Doe",
    age: 30,
    gender: "male",
    isEmployed: true,
    address: {
        street: "123 Main St",
        city: "Anytown",
        state: "CA",
        zipCode: "12345"
    },
    hobbies: ["reading", "hiking", "coding"],
    // Metode untuk mendapatkan nama lengkap
    getFullName: function() {
        return this.firstName + " " + this.lastName;
    },
    // Metode untuk memeriksa apakah orang tersebut sudah dewasa
    isAdult: function() {
        return this.age >= 18;
    }
};

function fullName(person) {
    return person.firstName + " " + person.lastName;
}

// Contoh pemanggilan fungsi
console.log(fullName(person)); // Output: John Doe



// Mengakses properti objek
console.log("First Name:", person.firstName); // Output: First Name: John
console.log("Last Name:", person.lastName); // Output: Last Name: Doe
console.log("Age:", person.age); // Output: Age: 30
console.log("Gender:", person.gender); // Output: Gender: male
console.log("Employment Status:", person.isEmployed); // Output: Employment Status: true

// Mengakses properti objek bersarang
console.log("Address:", person.address.street, person.address.city, person.address.state, person.address.zipCode);
// Output: Address: 123 Main St Anytown CA 12345

// Mengakses array di dalam objek
console.log("Hobbies:", person.hobbies.join(", ")); // Output: Hobbies: reading, hiking, coding

// Menggunakan metode objek
console.log("Full Name:", person.getFullName()); // Output: Full Name: John Doe
console.log("Is Adult:", person.isAdult()); // Output: Is Adult: true
