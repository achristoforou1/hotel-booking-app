# TESTING.md

## Overview
This file documents the manual and automated testing carried out on the **Hotel Booking App** to ensure that all components function as intended and meet the project assessment criteria.

## 1. Form Testing

**Form:** `BookingForm`  
**Test Cases:**
- Valid form submission with all fields filled in.
- Invalid form submission when required fields (e.g. `full_name`, `room_type`) are missing.

**Tools Used:** Django `TestCase`  
**Location:** `booking/tests.py`

## 2. Model Testing

**Model:** `Booking`  
**Test Cases:**
- `__str__` method returns full name and room type in correct format.
- Field values are correctly stored and retrievable from the database.

**Tools Used:** Django `TestCase`  
**Location:** `booking/tests.py`

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

## 4. Admin Panel

- Admin panel is set up and accessible.
- `Booking` model appears in the admin panel.
- Booking entries can be viewed, added, and deleted.

## 5. Manual Front-End Testing

**Homepage**
- Loads without error.
- Displays welcome message and “Make a Booking” link.

**Booking Form Page**
- Loads correctly in browser.
- Form validation works for required fields and date logic (e.g., check-out after check-in).
- Submits successfully and redirects.

**Success Page**
- Displays confirmation message after booking.

**Admin Panel**
- Verified booking entries appear after submission.

**My Bookings Page**
- Displays only the currently logged-in user’s bookings.

**Edit/Delete Pages**
- Only accessible when logged in and only for that user's booking.
- Redirect or error shown if trying to access someone else’s.

## 6. Testing Tools

- Python 3.12  
- Django 5.2.3  
- VS Code with Django extension  
- Browser: Chrome (latest)  
- Manual testing and `python manage.py test`

## 7. Summary

All critical components have been tested both manually and using Django’s built-in testing tools. The system behaves as expected across form validation, data handling, and user interaction routes.

## 8. User Authentication

**Registration**
- Visit `/accounts/signup/` and register a new user.
- Required fields must be filled in, and submission redirects to homepage.

**Login**
- Visit `/accounts/login/`, enter valid credentials, and confirm successful login.

**Logout**
- Click logout and confirm redirection to login page.

**Access Restrictions**
- Attempt to access `/book/`, `/my-bookings/`, `/edit/.../`, or `/delete/.../` without being logged in.
- Confirm redirection to login page as expected.

## 9. Booking CRUD Manual Testing

**Create Booking**
- Navigate to `/book/`, fill in and submit the form.
- Confirm redirect to success page and entry appears in admin panel.

**Read Bookings**
- Visit `/my-bookings/` while logged in.
- Confirm the list shows only that user's bookings.

**Update Booking**
- Click “Edit” on a booking from `/my-bookings/`.
- Submit updated data and verify changes are saved.

**Delete Booking**
- Click “Delete” on a booking from `/my-bookings/`.
- Confirm deletion and redirection to updated bookings list.

## 10. Custom Validation

**Check-out Before Check-in**
- Submit form with check-out earlier than check-in.
- Confirm appropriate error message appears.

## 11. Summary

All key features — authentication, booking creation and management, and validation — have been thoroughly tested. Testing was performed manually and programmatically using Django's test suite.

The system is stable, secure, and ready for final deployment.

## 12. Manual Testing Checklist

| Feature                        | Status | Notes |
|-------------------------------|--------|-------|
| Home page loads correctly     | OK     | Welcome message and link visible |
| User registration             | ✅     | New user can sign up via allauth |
| User login/logout             | ✅     | Login redirects correctly; logout returns to login page |
| Booking form submission       | ✅     | Form submits successfully with valid data |
| Invalid form handling         | ✅     | Errors shown for missing or incorrect data |
| Date validation (check-in/out)| ✅     | Error shown when check-out is before check-in |
| View my bookings              | ✅     | Only shows bookings for logged-in user |
| Edit my booking               | ✅     | Booking updates saved and reflected |
| Delete my booking             | ✅     | Booking removed and list updated |
| Access restriction (unauth)   | ✅     | Redirects to login if user not authenticated |
| Prevent editing others' data  | ✅     | Users cannot edit or delete others' bookings |
| Admin panel access            | ✅     | Booking model editable in admin |
| Responsive layout             | ✅     | Pages display correctly on desktop and mobile |




**Ready for deployment.**
