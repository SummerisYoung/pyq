<template>
  <div id="app">
    <div id="nav">
      <div v-if="this.$route.path == '/'">登录</div>
      <div v-else>
        <img alt="Vue logo" src="./assets/logo.png">
      </div>
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  data(){
    return {
      nickname:''//用户名
    }
  }, 
  mounted(){
    this.nickname = localStorage.nickname
  }
}
</script>

</script>
<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  font-size: 24px;
}

#nav a {
  color: black;
  text-decoration: none;
}
</style>
