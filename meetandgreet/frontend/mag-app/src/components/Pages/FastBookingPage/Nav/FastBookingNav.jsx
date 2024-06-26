import styles from "./FastBookingNav.module.css";
import Navigation from "./Navigation/Navigation";

export default function FastBookingNav() {
  return (
    <div className={styles.fast__nav}>
      <Navigation />
    </div>
  );
}
