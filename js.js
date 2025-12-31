if (window.location.pathname.includes("home.html")) {
let question = confirm("האם אתה רוצה להמשיך בקניה שלך ")
if (!question) {
    localStorage.removeItem('bag');
    localStorage.removeItem('sumBag');
    localStorage.removeItem("discountLevel")

}
}
let locaSumBag = localStorage.getItem('sumBag')
if (!locaSumBag) {
    let sum = 0;
    localStorage.setItem('sumBag', JSON.stringify(sum));
  }
  

// אתחול רמת ההנחות
if (!localStorage.getItem("discountLevel")) {
    localStorage.setItem("discountLevel", "0");
}

let sumBag = document.querySelector('#sumBag')
let sum = JSON.parse(localStorage.getItem('sumBag'));


sumBag.innerText = sum;

let basket = JSON.parse(localStorage.getItem('bag')) || [];





document.addEventListener('DOMContentLoaded',(event)=>{//לאחר טעינת קובץ איצ טי אמ אל מפעיל את הפונקציה פץ אייטם
    fetchItems();
});



 let container = document.querySelector('.container');

async function fetchItems(){
   
    const response = await fetch('http://127.0.0.1:5000/api/item/get_items');
    const items = await response.json();
    product = items;
  
    items.forEach(element => {//עוברים בלולאה על הפריטים

    shoeproduct(element)
  
    });
}


function shoeproduct(item) {
    const urlImage="http://127.0.0.1:5000/api/item/get_img/"+item.img

    let name = document.createElement('h1');
    name.style.textAlign = "center";
    let img = document.createElement('img');
    img.style.display = "block";
    img.style.margin = "0 auto";
    let cost = document.createElement('h2');
    cost.style.textAlign = "center";
    let div = document.createElement('div');
    let btnplus = document.createElement('button');
    let btnmin = document.createElement('button');
    let category=document.createElement('h3')
    category.style.textAlign = "center";
    btnplus.innerText = '+';
    btnmin.innerText = '-';


    
   
    btnplus.addEventListener('click', function (e) {
        btnmin.removeAttribute("disabled")
        plus(e, item)
    });
    btnmin.addEventListener('click', function (e) {
        
            minus(e, item)
    });
    name.innerHTML = item.name;
    img.src = urlImage;//.argument..קריאת APU לפייתון להחזיר את התמונה בקידוד בינארי
    img.style.width = '250px'
    cost.innerHTML = item.price;
    category.innerHTML = item.company_name;
    div.appendChild(name);
    div.appendChild(img);
    div.appendChild(category);
    div.appendChild(cost);
    div.appendChild(btnplus);
    div.appendChild(btnmin);
    
    container.appendChild(div);
}function shoeproductInBasket(item) {
    let allbasket = document.querySelector('.conteinerBasket');

    // יצירת אלמנטים חדשים + עיצוב בסיסי להפרדה
    let div = document.createElement('div');
    div.style.border = '1px solid #ccc';
    div.style.margin = '10px 0';
    div.style.padding = '10px';
    div.style.textAlign = 'center';
    div.style.direction = 'rtl'; //  יישור לימין

    let name = document.createElement('h3');
    let img = document.createElement('img');
    let costPerUnit = document.createElement('p'); 
    let cnt = document.createElement('h4'); 
    let totalCostItem = document.createElement('h4'); 

    let btnplus = document.createElement('button');
    let btnmin = document.createElement('button');
    
    // הגדרת תוכן
    name.innerHTML = item.name;
    
    img.src = "http://127.0.0.1:5000/api/item/get_img/" + item.img; 
    img.style.width = '100px';
    
    costPerUnit.innerHTML = `מחיר ליחידה: ${item.price} ש"ח`;
    cnt.innerHTML = `כמות: ${item.quantity}`; // מציג את הכמות
    
    let total = item.price * item.quantity;
    totalCostItem.innerHTML = `סה"כ לפריט: ${total.toFixed(2)} ש"ח`; // מחיר כולל לפריט
    
    btnplus.innerText = '+';
    btnmin.innerText = '-';
    
    // listener - קוראים לפונקציה refreshBasketDisplay לאחר העדכון
    btnplus.addEventListener('click', function (e) {
        plus(e, item);
        refreshBasketDisplay(); 
    });
    btnmin.addEventListener('click', function (e) {
        minus(e, item);
        refreshBasketDisplay(); 
    });
    
    // הוספת האלמנטים
    div.appendChild(name);
    div.appendChild(img);
    div.appendChild(costPerUnit);
    div.appendChild(cnt); 
    div.appendChild(totalCostItem); 
    div.appendChild(btnmin);
    div.appendChild(btnplus);

    allbasket.appendChild(div);
}

if (window.location.pathname.includes("bag.html")) {
    document.addEventListener('DOMContentLoaded', (event) => {
        refreshBasketDisplay();
    });
}

function plus(e, i) {

    // בדיקה: האם אין מספיק מלאי?
    let basket = JSON.parse(localStorage.getItem("bag")) || [];
    let itemInBasket = basket.find(x => x.id === i.id);

    let quantityInCart = itemInBasket ? itemInBasket.quantity : 0;

    if (quantityInCart >= i.count) {
        alert("אין מספיק מלאי למוצר זה");
        return;
    }


    // אם יש מלאי — ממשיכים כרגיל
    // מגדילים את הכמות בעגלה

    let sum = parseFloat(localStorage.getItem("sumBag")) || 0;
    sum += i.price;

    let discountLevel = parseInt(localStorage.getItem("discountLevel"));
    let nextLevel = (discountLevel + 1) * 1000;

    if (sum >= nextLevel) {
        sum -= 50;
        discountLevel++;
        localStorage.setItem("discountLevel", discountLevel);
        alert("קיבלת הנחה של 50 ש״ח!");
    }

    localStorage.setItem("sumBag", JSON.stringify(sum));
    sumBag.innerText = sum;

    // עדכון סל
    let addbasket = JSON.parse(localStorage.getItem("bag")) || [];

    let exist = addbasket.find(x => x.id === i.id);

    if (exist) {
        exist.quantity++;
    } else {
        addbasket.push({ ...i, quantity: 1 });
    }

    localStorage.setItem("bag", JSON.stringify(addbasket));
}


function minus(e, i) {
   
        let index = -1;
        minusbasket = localStorage.getItem("bag");
        if (minusbasket != '') {
            minusbasket = JSON.parse(minusbasket);
            for (let item = 0; item < minusbasket.length; item++) {//לולאה שבודקת אם קיים לי מוצר כזה בעגלה
                if (minusbasket[item].id == i.id) {//אם קיים, רק אשנה את הכמות
                    let sum = JSON.parse(localStorage.getItem('sumBag'));
                    sum -= i.price;
                    sumBag.innerText = sum;
                    localStorage.setItem("sumBag", JSON.stringify(sum));

                     // ביטול הנחה אם הסכום ירד מתחת לרף
let discountLevel = parseInt(localStorage.getItem("discountLevel"));

if (discountLevel > 0) {
    let requiredLevel = discountLevel * 1000;

    // אם ירדנו מתחת לרמת ההנחה
    if (sum < requiredLevel) {
        sum += 50;  // מחזירים את ההנחה
        discountLevel--;

        localStorage.setItem("discountLevel", discountLevel);
        localStorage.setItem("sumBag", JSON.stringify(sum));
        sumBag.innerText = sum;

        alert("ההנחה בוטלה מאחר וסכום הקנייה ירד מתחת לרף");
    }
}
                     
                    if (minusbasket[item].quantity == 1) {
                        index = item;
                        minusbasket.splice(index, 1);
                        minusbasket = JSON.stringify(minusbasket);

                        localStorage.setItem("bag", minusbasket)
                    }
                    else {
                        minusbasket[item].quantity -= 1;
                        minusbasket = JSON.stringify(minusbasket);
                        localStorage.setItem("bag", minusbasket);
                    }

                }

            }
        }

    }


const searchlmg = document.querySelector('#search');
const categorySelect = document.querySelector('#category');
searchlmg.addEventListener('click', function () {
    if (categorySelect.style.visibility == "hidden")
    categorySelect.style.visibility = "visible"

else {
    categorySelect.style.visibility = "hidden"


}
})
let choose = null;
categorySelect.addEventListener('change', () => {
    choose = categorySelect.value;
    container.innerHTML = "";
    if (choose == 'הכל') {
        for (let i = 0; i < product.length; i++) {

            shoeproduct(product[i])
        }
    }
    else {
        for (let i = 0; i < product.length; i++) {
            

    
            if (product[i].category_name == choose)
                shoeproduct(product[i])
        }
    }


})
let cart = document.querySelector('#bug');
cart.addEventListener('click', function () {
    window.open('bag.html', '_blank', 'width=400,height=600,top=0,left=0');

});
  
// פונקציה לרענון כל תצוגת הסל ב-bag.html
function refreshBasketDisplay() {
    let allbasket = document.querySelector('.conteinerBasket');
    allbasket.innerHTML = ''; // ניקוי התצוגה הקיימת

    let currentBasket = JSON.parse(localStorage.getItem('bag')) || [];

    // הצגת כל הפריטים מחדש
    currentBasket.forEach(item => {
        shoeproductInBasket(item);
    });

    // עדכון הסכום הכולל
    let sumBag = document.querySelector('#sumBag');
    let sum = JSON.parse(localStorage.getItem('sumBag')) || 0;
    sumBag.innerText = sum.toFixed(2);
    
}
window.addEventListener("storage", () => {
    let updatedSum = JSON.parse(localStorage.getItem("sumBag")) || 0;
    sumBag.innerText = updatedSum;
});
