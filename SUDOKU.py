import React, { useState } from "react";
import Navbar from "./Navbar";
import HeroSection from "./HeroSection";
import Portfolio from "./Portfolio";
import TemperatureConverter from "./TemperatureConverter";
import JokeFetcher from "./JokeFetcher";
import GuessingGame from "./GuessingGame";
import ContactManager from "./ContactManager";
import SudokuSolver from "./SudokuSolver";
import Footer from "./Footer";

const App = () => {
  // States to track which app modal to show
  const [showTemperatureConverter, setShowTemperatureConverter] = useState(false);
  const [showJokeFetcher, setShowJokeFetcher] = useState(false);
  const [showGuessingGame, setShowGuessingGame] = useState(false);
  const [showContactManager, setShowContactManager] = useState(false);
  const [showSudokuSolver, setShowSudokuSolver] = useState(false);

  // Handle which project (app) is clicked
  const handleProjectClick = (projectTitle) => {
    switch (projectTitle) {
      case "Temperature Converter":
        setShowTemperatureConverter(true);
        break;
      case "Joke App":
        setShowJokeFetcher(true);
        break;
      case "Guessing Game":
        setShowGuessingGame(true);
        break;
      case "Contact Manager":
        setShowContactManager(true);
        break;
      case "Sudoku Solver":
        setShowSudokuSolver(true);
        break;
      default:
        break;
    }
  };

  // Close all modals
  const closeModals = () => {
    setShowTemperatureConverter(false);
    setShowJokeFetcher(false);
    setShowGuessingGame(false);
    setShowContactManager(false);
    setShowSudokuSolver(false);
  };

  return (
    <div>
      <Navbar />
      <HeroSection />
      
      {/* Portfolio Section with the click handler */}
      <Portfolio onProjectClick={handleProjectClick} />
      
      {/* Modals for each app */}
      {showTemperatureConverter && <TemperatureConverter onClose={closeModals} />}
      {showJokeFetcher && <JokeFetcher onClose={closeModals} />}
      {showGuessingGame && <GuessingGame onClose={closeModals} />}
      {showContactManager && <ContactManager onClose={closeModals} />}
      {showSudokuSolver && <SudokuSolver onClose={closeModals} />}
      
      <Footer />
    </div>
  );
};

export default App;
