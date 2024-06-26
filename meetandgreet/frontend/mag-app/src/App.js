import React from "react";
import styles from "./App.module.css";
import MainPage from "./components/Pages/MainPage/MainPage.jsx";
import ServicesPage from "./components/Pages/ServisesPage/ServicesPage.jsx";
import { Route, Routes } from "react-router-dom";
// import FastBooking from "./components/Pages/Booking/Booking.jsx";
import LoginPage from "./components/Pages/LoginPage/LoginPage.jsx";
import TravelsPage from "./components/Pages/TravelsPage/TravelsPage.jsx";
import VipLoungePage from "./components/Pages/VipLoungePage/VipLoungePage.jsx";
import FastBookingPage from "./components/Pages/FastBookingPage/FastBookingForm.jsx";
import Cities from "./components/Pages/FastBookingPage/Cities/Cities.jsx";

function App() {
  return (
    <div className={styles.App}>
      <Routes>
        <Route path="/" exact element={<MainPage />} />
        <Route path="/servises" element={<ServicesPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/travels" element={<TravelsPage />} />
        <Route path="/vip_lounge" element={<VipLoungePage />} />
        <Route path="/fast_booking" element={<FastBookingPage />} />
        <Route path="/cities" element={<Cities />} />
      </Routes>
    </div>
  );
}

export default App;
