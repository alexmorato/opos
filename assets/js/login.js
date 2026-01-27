// login.js
// Centraliza la lógica de comprobación de usuario con bcryptjs para reutilización

const login = {
  async checkUserAuth(user_name, user_pass, requiredRole = null) {
    if (!user_name || !user_pass) {
      window.location.href = 'login.html';
      return;
    }
    try {
      // Buscar usuario en users.json
      const usersData = await fetch('assets/users.json').then(r => r.json());
      if (!usersData || !Array.isArray(usersData.users)) throw new Error('No users');
      const user = usersData.users.find(u => u.name === user_name);
      if (!user) throw new Error('No user');
      // Esperar a que bcryptjs esté disponible
      function waitForBcrypt() {
        return new Promise(resolve => {
          (function check() {
            if (window.dcodeIO && window.dcodeIO.bcrypt) resolve(window.dcodeIO.bcrypt);
            else if (window.bcryptjs) resolve(window.bcryptjs);
            else if (window.bcrypt) resolve(window.bcrypt);
            else setTimeout(check, 50);
          })();
        });
      }
      const bcrypt = await waitForBcrypt();
      if (!bcrypt.compareSync(user_pass, user.password_hash)) throw new Error('Bad pass');
      
      // Verificar rol requerido si se especifica
      if (requiredRole && Array.isArray(user.role) && !user.role.includes(requiredRole)) {
        throw new Error('Insufficient role');
      }
    } catch (e) {
      window.location.href = 'login.html';
    }
  }
};
