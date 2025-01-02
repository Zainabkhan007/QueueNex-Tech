from django.shortcuts import render,redirect
from .models import *
import pyrebase
from django.contrib import messages
config={
  "apiKey": "AIzaSyDfoVb8pRbKu6cOBpjjavLQ1xNQxmDsbxM",
  "authDomain": "test-29a14.firebaseapp.com",
  "databaseURL": "https://test-29a14-default-rtdb.firebaseio.com",
  "projectId": "test-29a14",
  "storageBucket": "test-29a14.firebasestorage.app",
  "messagingSenderId": "1076087987051",
  "appId": "1:1076087987051:web:62d833934f758fb4b78a2e",

}
firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
database=firebase.database()
# Create your views here.
def index(request):
    
    slide_title=database.child("Data").child("Title").get().val()
    slide_description=database.child("Data").child("description").get().val()
    slide2_title=database.child("Slider").child("Title").get().val()
    slide2_description=database.child("Slider").child("description").get().val()

    # About us 
    about_title=database.child("About Us").child("Title").get().val()
    about_description=database.child("About Us").child("description").get().val()
    return render(request, 'index.html',{
    "slide_title":slide_title,
    "slide_description":slide_description,
    "slide2_title":slide2_title,
    "slide2_description":slide2_description,
    "about_title":about_title,
    "about_description":about_description,

    })
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
           
            user = auth.sign_in_with_email_and_password(email, password)
            session_id = user['idToken']
            request.session['uid'] = str(session_id)  
            messages.success(request, "Login successful!")
            return redirect('index') 
            
        except Exception as e:
            
            messages.error(request, "Invalid credentials. Please try again.")
            return render(request, 'index.html')  
            
    else:
        return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
            # Firebase sign up
            user = auth.create_user_with_email_and_password(email, password)
            uid = user["localId"]
            data = {"username": username, "email": email, "password": password}
            
           
            database.child("users").child(uid).child("details").set(data)
            messages.success(request, "Signup successful! Please login.")
            return redirect('index')  
        except Exception as e:
            messages.error(request, f"Error during signup: {str(e)}")
            return render(request, 'signup.html')  
    else:
        return render(request, 'signup.html') 


def contact(request):
    if request.method == "POST":
       
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        contact_data = {
            "name": name,
            "email": email,
            "phone": phone,
            "message": message,
        }

        try:
           
            database.child("contact Us").push(contact_data)

            messages.success(request, "Your message has been sent successfully!")
            return redirect('index')  

        except Exception as e:
            
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('index')

    else:
        return redirect('index')