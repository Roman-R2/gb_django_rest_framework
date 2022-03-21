import React from "react";
import './App.css';
import axios from 'axios'
import Menu from "./components/menu";
import Footer from "./components/footer";
import UserList from "./components/user_list";
import {HashRouter, Route, Router} from "react-router-dom";


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      "users": [],
    }
  }

  // Этот метод будет вызван, когда компонент будет полностью смонтировано на экран
  // Тогда и идем за данными
  componentDidMount() {
    axios
      .get('http://127.0.0.1:8000/api/users/')
      .then(responce => {
        const users = responce.data.results
        // Поменяли состояние у реакта
        this.setState({
          'users': users
        })
      })
      .catch(error => console.log(error))
  }

  render() {
    return (
      <div>
        <Footer/>
        <Menu/>
        <UserList users={this.state.users}/>
      </div>
    )
  }
}

export default App;
