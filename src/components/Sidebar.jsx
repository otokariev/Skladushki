function Sidebar() {
  return (
    <aside>
      <h2 className="sidebar_">все пользователи</h2>

      <div className="sidebar_btn-box2">
        <button className="sidebar_btn">мужчины</button>
        <button className="sidebar_btn">женщины</button>
        <button className="sidebar_btn">создать анкету</button>
        <button className="sidebar_btn">войти</button>
      </div>
      <input className="sidebar_input" type="text" placeholder="искать..." />
    </aside>
  );
}

export default Sidebar;
