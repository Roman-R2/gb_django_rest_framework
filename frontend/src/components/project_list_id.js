import {Link, useParams} from "react-router-dom";

const ProjectItem = ({project}) => {
  return (
    <tr>
      <td>
        <Link to={`/${project.id}`}>{project.title}</Link>
      </td>
      <td>
        {project.repo_link}
      </td>
      <td>
        {project.users}
      </td>
    </tr>
  )
}

const ProjectListId = ({projects}) => {
  let {id} = useParams()
  let filteredProjects = projects.filter((projects) => projects.users.includes(parseInt(id)))

  return (
    <table>
      <th>
        Title
      </th>
      <th>
        Link to repo
      </th>
      <th>
        Users
      </th>
      {filteredProjects.map((project) => <ProjectItem project={project}/>)}
    </table>
  )
}

export default ProjectListId