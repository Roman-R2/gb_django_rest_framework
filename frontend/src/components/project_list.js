const ProjectItem = ({project}) => {
  return (
    <tr>
      <td>
        {project.title}
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

const ProjectList = ({projects}) => {
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
      {projects.map((project) => <ProjectItem project={project}/>)}
    </table>
  )
}

export default ProjectList