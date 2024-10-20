import React, { useState } from 'react';
import axios from 'axios';

const UserForm = ({ getUsers, selectedUser, clearSelection }) => {
  const [name, setName] = useState(selectedUser ? selectedUser.name : '');
  const [email, setEmail] = useState(selectedUser ? selectedUser.email : '');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    const userData = { name, email, password };

    if (selectedUser) {
      // Actualizar usuario
      axios.put(`http://localhost:5000/users/${selectedUser.id}`, userData)
        .then(() => {
          getUsers();
          clearSelection();
        });
    } else {
      // Crear nuevo usuario
      axios.post('http://localhost:5000/users', userData)
        .then(() => {
          getUsers();
        });
    }
    
    setName('');
    setEmail('');
    setPassword('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Nombre"
        value={name}
        onChange={(e) => setName(e.target.value)}
        required
      />
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      />
      <input
        type="password"
        placeholder="Contraseña"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
      />
      <button type="submit">
        {selectedUser ? 'Actualizar Usuario' : 'Crear Usuario'}
      </button>
      {selectedUser && <button onClick={clearSelection}>Cancelar</button>}
    </form>
  );
};

export default UserForm;
