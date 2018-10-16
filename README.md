# Khaidai
> restaurant-management-system.
> **Yet to complete some functionalities. But stopped the development.**
---

## Features
* Cart
* Order confirmation
* Promo Token
* Login/Registration
* **Restaurants**
	* Profile
	* Food menu
	* Rating/reviews
* Search
* My Orders Dashboard
* Notifications
* Profile
* My Reviews
* Admin Order management dashboard **(Only for superuser)**
* etc...
---

## Used Technologies
* Python
* Django v1.11
* SQLite3
* HTML
* CSS
* Bootstrap
* ClockPicker
* Font-Awesome
* JavaScript
	* **jQuery**
		* Ajax
	* Notify.js
	* jQueryMyCart.js
	* Wow.js
---

# Installation

### Create khaidai's virtual environment & goto the directory.
**Linux**
```bash
virtualenv -p /usr/bin/python3 khaidai
cd khaidai/
```
**Windows**
```bash
virtualenv khaidai
cd .\khaidai\
```

### Activate virtualenv
**Linux**
```bash
source bin/activate
```
**Windows**
```bash
.\Scripts\activate
```

**clone the project in the khaidai directory.**
```bash
git clone https://github.com/iraihankabir/restaurant-management.git
```

### Install reequirements.txt
```bash
python -m pip install -r requirements.txt
```

### rename restaurant-manager directory to 'src' **[optional]**.
```bash
mv restaurant-manager src/
```

### goto src directory and create db models.
```bash
cd src/
python manage.py migrate
```

### Run dev server at port 8888.
```bash
python manage.py runserver 8888
```
* now goto http://127.0.0.1:8888/
---

# SCREENSHOTS

## 01
![image](ss/home1.png)
---

## 02
![image](ss/home2.png)
---

## 03
![image](ss/right-menu.png)
---

## 04
![image](ss/profile-info.png)
---

## 05
![image](ss/mycart.png)
---

## 06
![image](ss/my-reviews.png)
---

## 07
![image](ss/notification-list.png)
---

## 08
![image](ss/restaurant-detail.png)
---

## 09
![image](ss/restaurant-foods.png)
---

## 10
![image](ss/restaurant-list.png)
---

## 11
![image](ss/restaurant-reviews.png)
---

## 12
![image](ss/order-confirm.png)
---

## 13
![image](ss/order-confirm-2.png)
---

## 14
![image](ss/order-dashboard.png)
---

## 15
![image](ss/order-detail.png)
---

