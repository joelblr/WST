# Web Scarper Tool

## Prerequisites
Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Setup Instructions

   #### All @ once
   ```bash
   git clone https://github.com/joelblr/WST-FKART.git
   cd WST-FKART\
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   python app.py

   ```
Follow these steps to set up and run the application:
1. **Clone the Project**
   ```bash
   git clone https://github.com/joelblr/WST-FKART.git
   ```
2. **Navigate to Project Directory**
   ```bash
   cd WST-FKART\
   ```
3. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   ```

4. Activate the Virtual Environment
   ##### On Windows:
      ```bash
      .\venv\Scripts\activate
      ```
   ##### On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
5. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```

6. Run the Application
   ```bash
   python app.py
   ```

## GUI Result
![image](https://github.com/user-attachments/assets/04b86c72-5d9a-47ed-8d0e-e98ad558b91a)


## Sample Input Data
##### base_url: https://www.flipkart.com/motorola-g84-5g-viva-magneta-256-gb/product-reviews/itmed938e33ffdf5?pid=MOBGQFX672GDDQAQ&lid=LSTMOBGQFX672GDDQAQSSIAM2&marketplace=FLIPKART
##### product_name: MOTOROLA g84 5G
##### cust_name: _2NsDsF AwS1CA
##### review_title: z9E0IG
##### rating: XQDdHH Ga3i8K
##### comment: ZmyHeo
##### num_pages: 25
##### filename: Test

## Sample Output Dataset
![image](https://github.com/user-attachments/assets/90b0e1a8-cd2c-41db-8314-9e2939ee2584)
