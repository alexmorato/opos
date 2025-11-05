// login.js
// Centraliza la lógica de comprobación de usuario con bcryptjs para reutilización

const login = {
  async checkUserAuth() {
    const user_guid = localStorage.getItem('user_guid');
    const user_pass = localStorage.getItem('user_pass');
    if (!user_guid || !user_pass) {
      window.location.href = 'index.html';
      return;
    }
    try {
      // Buscar usuario en users.json
      const usersData = await fetch('assets/users.json').then(r => r.json());
      if (!usersData || !Array.isArray(usersData.users)) throw new Error('No users');
      const user = usersData.users.find(u => u.guid === user_guid);
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
    } catch (e) {
      window.location.href = 'index.html';
    }
  }
};
