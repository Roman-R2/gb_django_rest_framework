import React from "react";
import './App.css';
import axios from 'axios'
import Menu from "./components/menu";
import Footer from "./components/footer";
import UserList from "./components/user_list";
import ProjectList from "./components/project_list";
import ProjectListId from "./components/project_list_id";
import {HashRouter, BrowserRouter, Route, Router, Routes, Link, useLocation, Navigate} from "react-router-dom";
import TodoList from "./components/todo_list";

const NotFound = () => {
  let location = useLocation()
  return (
    <div> Page {location.pathname} not found </div>
  )
}

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      "users": [],
      "projects": [],
      "todos": [],
    }
  }

  // Этот метод будет вызван, когда компонент будет полностью смонтировано на экран
  // Тогда и идем за данными
  componentDidMount() {
    axios
      .get('http://127.0.0.1:8000/api/users/')
      .then(responce => {
        const users = responce.data
        // Поменяли состояние у реакта
        this.setState({
          'users': users
        })
      })
      .catch(error => console.log(error))

    axios
      .get('http://127.0.0.1:8000/api/projects/')
      .then(responce => {
        const projects = responce.data
        // Поменяли состояние у реакта
        this.setState({
          'projects': projects
        })
      })
      .catch(error => console.log(error))

    axios
      .get('http://127.0.0.1:8000/api/todos/')
      .then(responce => {
        const todos = responce.data
        // Поменяли состояние у реакта
        this.setState({
          'todos': todos
        })
      })
      .catch(error => console.log(error))
  }

  render() {
    return (
      <div>
        <BrowserRouter>
          <Menu/>
          <Routes>
            <Route exact path='/' element={<ProjectList projects={this.state.projects}/>}/>
            <Route exact path='/projects' element={<Navigate to={'/'}/>}/>
            <Route exact path='/users' element={<UserList users={this.state.users}/>}/>
            <Route exact path='/todos' element={<TodoList todos={this.state.todos}/>}/>
            <Route path='/:id' element={<ProjectListId projects={this.state.projects}/>}/>
            <Route path="*" element={<NotFound/>}/>
          </Routes>
        </BrowserRouter>
        <Footer/>
      </div>
    )
  }
}

export default App;
