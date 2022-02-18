import React from "react";
import './App.css';
import AuthorList from "./components/author_list";
import axios from 'axios'
import Menu from "./components/menu";
import Footer from "./components/footer";
import UserList from "./components/user_list";


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      "authors": [],
      "users": [],
    }
  }

  // Этот метод будет вызван, когда компонент будет полностью смонтировано на экран
  // Тогда и идем за данными
  componentDidMount() {
    axios
      .get('http://127.0.0.1:8000/api/authors/')
      .then(responce => {
        const authors = responce.data

        // Поменяли состояние у реакта
        this.setState({
          'authors': authors
        })
      })
      .catch(error => console.log(error))

    axios
      .get('http://127.0.0.1:8000/api/todousers/')
      .then(responce => {
        const users = responce.data
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
        <AuthorList authors={this.state.authors}/>
        <UserList users={this.state.users}/>
      </div>
    )
  }
}

export default App;
