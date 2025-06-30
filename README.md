# BELLA VISTA - Hotel Booking App

Bella Vista is a responsive hotel booking web application designed for users seeking a smooth and intuitive experience when reserving accommodation. Built with Django, the site allows users to register, book hotel rooms, and manage their bookings entirely online.

The app is ideal for travellers who want to check availability and secure their reservations without having to call or email. It provides personalized functionality such as booking history, editing reservations, and user authentication for privacy and security.

## Responsively App

### Website across all screen sizes

![Responsive Mockup](/assets\images\responsively_bella_vista.png)

---

## Features

### Existing Features

- **Navigation Bar**
  - Present on all pages with links to login, signup, make a booking, view bookings, and logout.
  - Adjusts based on authentication status.

- **Homepage**
  - A visually appealing landing section with a hotel-themed background image and “Make a Booking” CTA button.
  - Welcomes users with a clear value proposition.

- **User Authentication**
  - Users can register, log in, and log out using Django Allauth.
  - Protected routes ensure users only manage their own bookings.

- **Booking Form**
  - Users can book a room with details like name, check-in/check-out dates, and room type.
  - The form includes date validation (e.g. check-in cannot be after check-out).

- **My Bookings Page**
  - Shows only the logged-in user’s bookings.
  - Includes options to edit or delete each booking.

- **Edit/Delete Booking**
  - Users can update their booking information or delete it entirely.
  - Validation and confirmation messages are displayed accordingly.

- **Admin Panel**
  - Site admin can manage all bookings via Django admin interface.

- **Responsive Layout**
  - Optimized for mobile, tablet, and desktop using Responsively App and browser dev tools.

### Features Left to Implement

- Confirmation email on successful booking.
- Calendar date picker for improved UX on mobile.
- Room availability checker to prevent double booking.

---

## Testing

### Manual Testing

Manual testing was performed on all user journeys including homepage, login, booking, and admin functionality. The layout and behavior were checked across multiple device sizes.

Detailed testing logs and outcomes are provided in the [TESTING.md](TESTING.md) file.

#### Known Bug
- Password reset form loads, but submission returns a 500 server error. This is noted and will be addressed post-deployment.

---

## Validator Testing

- **HTML**: Validated using [W3C HTML Validator](https://validator.w3.org/)
- **CSS**: Validated using [W3C CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/)

---

## Deployment

The site was deployed using [Heroku](https://heroku.com) with the following steps:

1. Set up `requirements.txt` and `Procfile`.
2. Configure the Heroku app with PostgreSQL and `DATABASE_URL`.
3. Push code to Heroku via GitHub integration.
4. Set `DEBUG = False` and configure `ALLOWED_HOSTS`.
5. Uploaded media stored using Cloudinary.
6. Final deployment URL: [https://hotel-booking-app-anthony-310db2860612.herokuapp.com/](https://hotel-booking-app-anthony-310db2860612.herokuapp.com/)

---

## Credits

### Content

- Custom content was written based on real-world hotel booking workflows.
- Form validation logic was assisted by Django documentation and Stack Overflow examples.

### Media

- Background image used across the app: [pexels.com](https://pexels.com/)
- Favicon and icons: [Font Awesome](https://fontawesome.com/)

---

