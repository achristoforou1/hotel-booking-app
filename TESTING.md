# TESTING.md

## Overview
This file documents the manual and automated testing carried out on the **Hotel Booking App** to ensure that all components function as intended and meet the project assessment criteria.

---

## 1. Form Testing

**Form:** `BookingForm`  
**Test Cases:**
- Valid form submission with all fields filled in.
- Invalid form submission when required fields (e.g. `full_name`, `room_type`) are missing.

**Tools Used:** Django `TestCase`  
**Location:** `booking/tests.py`

---

## 2. Model Testing

**Model:** `Booking`  
**Test Cases:**
- `__str__` method returns full name and room type in correct format.
- Field values are correctly stored and retrievable from the database.

**Tools Used:** Django `TestCase`  
**Location:** `booking/tests.py`

---

## 3. View Testing

**View:** `booking_view`  
**Test Cases:**
- `GET` request returns the correct form template.
- `POST` request with valid data redirects to success page.

**View:** `booking_success`  
**Test Case:**
- `GET` request returns the correct success message and template.

**Tools Used:** Django `TestCase`  
**Location:** `booking/tests.py`

---

## 4. Admin Panel

- Admin panel is set up and accessible.
- `Booking` model appears in the admin panel.
- Booking entries can be viewed, added, and deleted.

---

## 5. Manual Front-End Testing

**Booking Form Page**
- Loads correctly in browser.
- Form input validation triggers on empty required fields.
- Submission redirects to success page.

**Success Page**
- Displays confirmation message.

**Admin Panel**
- Verified booking entries appear after submission.

---

## 6. Testing Tools

- Python 3.12  
- Django 5.2.3  
- VS Code with Django extension  
- Browser: Chrome (latest)  
- Manual testing and `python manage.py test`

---

## 7. Summary

All critical components have been tested both manually and using Django’s built-in testing tools. The system behaves as expected across form validation, data handling, and user interaction routes.

**Ready for deployment.**
