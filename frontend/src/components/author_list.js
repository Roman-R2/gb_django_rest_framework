const AuthorItem = ({author}) => {
  return (
    <tr>
      <td>
        {author.first_name}
      </td>
      <td>
        {author.last_name}
      </td>
      <td>
        {author.dirthday_year}
      </td>
    </tr>
  )
}

const AuthorList = ({authors}) => {
  return (
    <table>
      <th>
        First Name
      </th>
      <th>
        Last name
      </th>
      <th>
        Birth year
      </th>
      {authors.map((author) => <AuthorItem author={author}/>)}
    </table>
  )
}

export default AuthorList