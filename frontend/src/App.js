import React, { useState, useEffect } from 'react';
import axios from 'axios';
import UserForm from './components/UserForm';
import UserList from './components/UserList';

const App = () => {
  const [users, setUsers] = useState([]);
  const [selectedUser, setSelectedUser] = useState(null);

  const getUsers = () => {
    axios.get('http://localhost:5000/users')
      .then(response => {
        setUsers(response.data);
      });
  };

  useEffect(() => {
    getUsers();
  }, []);

  const clearSelection = () => {
    setSelectedUser(null);
  };

  return (
    <div>
      <h1>Gestión de Usuarios</h1>
      <UserForm getUsers={getUsers} selectedUser={selectedUser} clearSelection={clearSelection} />
      <UserList users={users} getUsers={getUsers} setSelectedUser={setSelectedUser} />
    </div>
  );
};

export default App;
