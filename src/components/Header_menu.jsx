
function Header_menu() {
  return (
    <nav>
      <ul className="header_menu-box">
        <li className="header_menu-item">
          <a href="" className="Header_menu-link">о нас</a>
        </li>
        <li className="header_menu-item">
          <a href="" className="Header_menu-link">контакты</a>
        </li>
        <li className="header_menu-item">
          <button className="header_btn">создать анкету</button>
        </li>
        <li className="header_menu-item">
          <button className="header_btn" onClick={function(){
            console.log('header_btn');
          }}>войти</button>
        </li>
      </ul>
    </nav>
  );
}

export default Header_menu;
