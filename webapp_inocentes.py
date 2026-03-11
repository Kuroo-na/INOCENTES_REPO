import streamlit as st
import datetime

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["About", "Search Hotels", "Booking"])

# About Page
if page == "About":
    st.title("Hotel Booking Site")
    st.write("This site helps Travelers book hotels quickly.")
    st.write("Target users: Travelers looking for easy reservations.")
    st.write("Inputs: location, dates, guests.")
    st.write("Outputs: hotel suggestions and booking confirmation.")

# Search Hotels
elif page == "Search Hotels":
    st.title("Search Hotels")
    location = st.selectbox("Choose a location:", ["Manila", "Taguig", "Makati"])
    check_in = st.date_input("Check-in Date:", datetime.date.today())
    check_out = st.date_input("Check-out Date:", datetime.date.today() + datetime.timedelta(days=1))
    guests = st.number_input("Number of guests:", 1, 10, 2)

    if st.button("Search"):
        st.success(f"Hotels found in {location} from {check_in} to {check_out}.")
        hotels = ["Hotel Sunshine", "Ocean View Resort", "City Lights Inn"]
        for h in hotels:
            if st.button(f"Book {h}"):
                st.session_state['booked_hotel'] = h
                st.success(f"You selected {h}. Go to Booking page to confirm.")

# Booking Page
elif page == "Booking":
    st.title("Book Your Room")
    hotel = st.selectbox("Select a hotel:", ["Hotel Sunshine", "Ocean View Resort", "City Lights Inn"])
    nights = st.number_input("Number of nights:", min_value=1, max_value=30, value=2)
    guests = st.number_input("Number of guests:", min_value=1, max_value=10, value=1)
    extras = st.multiselect("Add extras:", ["Airport Pickup", "Spa Access", "Breakfast Buffet"])
    st.file_uploader("Upload your ID for verification:")
    if st.button("Confirm Booking"):
        st.success(f"Booking confirmed at {hotel} for {nights} nights, {guests} guest(s). Extras: {', '.join(extras)}")