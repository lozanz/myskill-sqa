var car = {
    // properti
    type: "Fiat",
    model: "500",
    color: "white",
    // method
    start: function(){
        console.log("ini method start");
        },
    drive: function(){
        console.log("ini method drive");
        },
    brake: function(){
        console.log("ini method brake");
        },
    stop: function(){
        console.log("ini method stop");
        }
        };

// akses Object
console.log(car.type);
//Result "Fiat"
console.log(car.color);
//Result "white"
car.start();
//Result "ini method start"
car.drive();
//Result "ini method drive"

// penggunaan keyword this
function Person(firstName, lastName){
    // properti
    this.firstName = firstName;
    this.lastName = lastName;
    // method
    this.fullName = function(){
        return `${this.firstName} ${this.lastName}`
}
this.showName = function(){
console.log(this.fullName());
}
}
var person1 = new Person("Muhar", "Dian");
var person2 = new Person("Petani", "Kode");
person1.showName();
person2.showName();