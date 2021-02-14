from selenium import webdriver
from flask import Flask, render_template, request, jsonify
import os
app = Flask(__name__)

loc = os.getcwd() + "/chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
#chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage") 
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=loc, chrome_options=chrome_options)

@app.route("/")
def home():
    print("running home def")
    #link = input("amazon link? ")
    #driver.get(link)
    return render_template("index.html")

@app.route("/OpenFile", methods=["POST"])
def openFile():
    print("opening files amazon link def")
    link = request.form["link"]
    driver.get(link)
    try:
        price = driver.find_element_by_id("priceblock_ourprice")
        print(price.text)
    except:
        print("couldnt find price")

    amount = price.text

    return jsonify(amount)

if __name__ == "__main__":
    app.run()