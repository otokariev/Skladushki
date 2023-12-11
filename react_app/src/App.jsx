import "./App.css";
import Footer from "./components/Footer";
import Header from "./components/Header";
import Main from "./components/Main";
import Sidebar from "./components/Sidebar"
function App() {
  return (
    <>
      <Header />
      <div className="main__wrap">
      <Sidebar/>
      <Main />
      </div>
      <Footer />
    </>
  );
}

export default App;
