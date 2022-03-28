import React from "react";
import './App.css';
import axios from 'axios'
import Footer from "./components/footer";
import UserList from "./components/user_list";
import ProjectList from "./components/project_list";
import ProjectListId from "./components/project_list_id";
import LoginForm from "./components/LoginForm";
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
      'token': ''
    }
  }

  getData() {
    let headers = this.getHeader()

    axios
      .get('http://127.0.0.1:8000/api/users/', {headers})
      .then(responce => {
        const users = responce.data
        // Поменяли состояние у реакта
        this.setState({
          'users': users
        })
      })
      .catch(error => {
        console.log(error)
        this.setState({
          'users': []
        })
      })

    axios
      .get('http://127.0.0.1:8000/api/projects/', {headers})
      .then(responce => {
        const projects = responce.data
        // Поменяли состояние у реакта
        this.setState({
          'projects': projects
        })
      })
      .catch(error => {
        console.log(error)
        this.setState({
          'projects': []
        })
      })

    axios
      .get('http://127.0.0.1:8000/api/todos/', {headers})
      .then(responce => {
        const todos = responce.data
        // Поменяли состояние у реакта
        this.setState({
          'todos': todos
        })
      })
      .catch(error => {
        console.log(error)
        this.setState({
          'todos': []
        })
      })
  }

  // Этот метод будет вызван, когда компонент будет полностью смонтировано на экран
  // Тогда и идем за данными
  componentDidMount() {
    let token = localStorage.getItem('token')
    this.setState({
      'token': token
    }, this.getData)
  }

  isAuth() {
    return !!this.state.token
  }

  getHeader() {
    if (this.isAuth()) {
      return {
        'Authorization': 'Token ' + this.state.token
      }
    }
    return {}
  }

  getToken(login, password) {
    // console.log(login, password)
    axios
      .post('http://127.0.0.1:8000/api-auth-token/', {'username': login, 'password': password})
      .then(response => {
        const token = response.data.token
        // console.log(token)
        localStorage.setItem('token', token)
        this.setState({
          'token': token
        }, this.getData)
      })
      .catch(error => console.log(error))
  }

  logout() {
    localStorage.setItem('token', '')
    this.setState({
      'token': ''
    }, this.getData)
  }

  render() {
    return (
      <div>
        <BrowserRouter>
          <nav>
            <li><Link to='/'>Projects</Link></li>
            <li><Link to='/users'>Users</Link></li>
            <li><Link to='/todos'>Todos</Link></li>
            <hr/>
            <li>
              {this.isAuth() ? <button onClick={() => this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
            </li>
          </nav>
          <Routes>
            <Route exact path='/' element={<ProjectList projects={this.state.projects}/>}/>
            <Route exact path='/projects' element={<Navigate to={'/'}/>}/>
            <Route exact path='/users' element={<UserList users={this.state.users}/>}/>
            <Route exact path='/todos' element={<TodoList todos={this.state.todos}/>}/>
            <Route exact path='/login'
                   element={<LoginForm getToken={(login, password) => this.getToken(login, password)}/>}/>
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
