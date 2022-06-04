# Teenager-Renting-backend
**购物车页面**

1. GET url: http://127.0.0.1:8000/cart   parameter: uid
2. POST url: http://127.0.0.1:8000/cart/submit/  parameters: uid hid type order_time duration amount detail
3. POST url: http://127.0.0.1:8000/cart/delete/  parameters: uid hid


**我的订单页面**

1. GET url: http://127.0.0.1:8000/order/  parameters: uid
2. GET url: http://127.0.0.1:8000/order/get_paid/  parameters: uid
3. GET url: http://127.0.0.1:8000/order/get_unpaid/  parameters: uid
4. POST url: http://127.0.0.1:8000/order/pay/  parameters: uid oid
5. POST url: http://127.0.0.1:8000/order/cancel/  parameters:uid oid
6. POST url: http://127.0.0.1:8000/order/delete/  parameters:uid oid

**主页**

1. GET url: http://127.0.0.1:8000/homepage/get_user/  parameters: uid
2. GET url: http://127.0.0.1:8000/homepage/get_house/  parameters: None
3. GET url: http://127.0.0.1:8000/homepage/get_data/  parameters: None


**个人主页**

1. GET url: http://127.0.0.1:8000/personal_homepage/get_cart/  parameters: uid
2. GET url: http://127.0.0.1:8000/personal_homepage/get_house/  parameters: None
3. GET url: http://127.0.0.1:8000/personal_homepage/get_user/  parameters: uid


**房源列表页面**

1. GET url: http://127.0.0.1:8000/browse_house/search/  parameters: keywords
2. GET url: http://127.0.0.1:8000/browse_house/get_user/ parameters:uid


**房源详情页面**

1. GET url: http://127.0.0.1:8000/browse_house/get_house/  parameters: hid
2. GET url: http://127.0.0.1:8000/browse_house/get_user/  parameters: uid
