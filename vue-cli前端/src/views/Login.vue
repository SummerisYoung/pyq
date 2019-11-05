<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <div class="login">
      <div>请输入用户名：<input v-model="nickname" type="text"></div>
      <div>请输入密码：<input style="margin-left:16px" v-model="password" type="password"></div>
      <div style="margin:0 40%"><input type="submit" value="登录" @click="login"></div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import Qs from 'qs'
export default {
  name: 'login',
  data(){
    return {
      nickname:'',
      password:'',
    }
  },
  methods:{
    login(){
      var that = this
      let data = {
        'nickname':that.nickname,
        'password':that.password,
      }
      console.log(that.nickname,that.password)
      //axios.post的url必须写全地址，不然url会给你在前面默认加上http://localhost/，这样就找不到服务器地址了。
      //请求后端需要加上请求头headers解决跨域问题。
      //data数据要用Qs将参数转为query参数，不然后端获取不到参数
      axios.post('http://127.0.0.1:8000/app/login',Qs.stringify(data),{
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      }).then(function(res){
        console.log(res)
        if(res.data == 'user is not exist!'){
          alert('用户不存在!')
        }else if(res.data == 'password mistake!'){
          alert('密码错误')
        }else{
          alert('登录成功!')
          localStorage.userid = res.data.user_id//保存id到本地缓存
          localStorage.nickname = that.nickname//保存用户名到本地缓存
          that.$router.push({
            name:'pyq',
          })
        }
      }).catch(function (error) {
        console.log(error);
      });
    }
  }
}
</script>

<style scoped>
.login{
  border: 1px solid #ddd;
  padding: 5%;
  margin: 5vh auto 0;
  width:80%;
  height: 15vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-start;
}
</style>