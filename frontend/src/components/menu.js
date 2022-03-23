import {Link} from "react-router-dom";
import React from "react";

const Menu = () => {
  return (
    <nav>
            <li><Link to='/'>Projects</Link></li>
            <li><Link to='/users'>Users</Link></li>
          </nav>

  )
}

export default Menu