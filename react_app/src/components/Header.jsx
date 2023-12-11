import Header_menu from "./Header_menu"


function Header() {
  return (
    <header className="header">
      <h1><a className="header__logo" href="">Skladushki</a></h1>
      <Header_menu/>
    </header>
  )
}

export default Header
