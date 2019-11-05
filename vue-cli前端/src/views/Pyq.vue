<template>
  <div class="about">
    <div class="title">
        <router-link to="/Write" >{{nickname}}的朋友圈</router-link>
        <span class="exit" @click="exit">退出登录</span>
    </div>
    <div class="main">
      <div class="pyq" v-for="(pyq,p) in pyqs" :key="p">
        <div style="color:#4a77ad;font-weight:600">{{pyq.wx_user.nickname}}</div>
        <div style="margin: 10px 0;text-align:left">{{pyq.content}}</div>
        <div style="margin: 10px 0;width:100%;display:flex;justify-content:space-between">
          <div>
            {{pyq.time}}
          </div>
          <modal title="提示" content="确认删除吗？" @on-cancel="cancelModal()" @on-confirm="confirmModal()" v-show='showModal'></modal>
          <div class="delete" v-if="pyq.wx_user.id == userid" @click="deleteModal(pyq.id)">删除</div>
          <div class="comment_operator" @click="comment(pyq.id)">评论</div>
        </div>
        <!-- 这里使用了vue的transition标签和animate.css结合 -->
        <transition enter-active-class="animate bounceIn" leave-active-class="animate bounceOut">
          <div v-show="showInput && pyq.id == i" style="width:100%;display:flex;justify-content:space-between;align-items:center">
            <input v-model="reviewContent" class="commentInput" type="text" placeholder="评论">
            <span class="sendBtn" @click="sendComment(pyq.id)">发送</span>
          </div>
        </transition>

        <div v-if="pyq.review.length" class="comment">
          <div style="margin: 10px 0;text-align:left" v-for="(review,r) in pyq.review" :key="r">
            <span style="color:#4a77ad;font-weight:600">{{review.wx_user.nickname}}</span>:{{review.comments}}
          </div>
        </div>
      </div>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data(){
    return {
      pyqs:[],
      userid:localStorage.userid,//登录用户
      nickname:localStorage.nickname,
      showModal:false,//是否显示模态框
      deleteId:null,//要删除的朋友圈id
      showInput:false,//是否显示评论框
      i:-1,//判别评论哪个朋友圈的id
      reviewContent:''//评论内容
    }
  },  
  mounted(){
    this.pyq()
  },
  methods:{
    pyq(){
      var that = this
      console.log(localStorage)
      axios.get('http://127.0.0.1:8000/app/pyq?userid='+localStorage.userid,{
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      }).then(function(res){
        if(res.data){
          for(let r of res.data){
            that.pyqs.push(r)
          }
        }
        console.log('朋友圈',that.pyqs)
      }).catch(function (error) {
        console.log(error)
      });
    },
    exit(){
      this.$router.push({
        name:'login'
      })
    },
    deleteModal(id){
      this.deleteId = id
      this.showModal = true
    },
    cancelModal(){
      this.showModal = false
    },
    confirmModal(){
      var that = this
      axios.post('http://127.0.0.1:8000/app/pyq',{
        id:that.deleteId
      }).then(function(res){
        if(res.data == "delete success!"){
          alert("删除成功!")
        }
        that.showModal = false
        location.reload()
      }).catch(function(error){
        console.log(error)
      })
    },
    comment(index){
      this.i = index
      this.showInput = !this.showInput
    },
    sendComment(pyqid){
      console.log(pyqid)
      var now = new Date()
      var t = now.getFullYear() + '-' + (now.getMonth() + 1) + '-' + now.getDate() + ' '
        + now.getHours() + ':' + now.getMinutes() + ':' + now.getSeconds()
      var that = this
      axios.post('http://127.0.0.1:8000/app/review',{
        pyqid:pyqid,
        userid:that.userid,
        comments:that.reviewContent,
        time:t
      }).then(function(res){
        console.log(res)
        location.reload()
      }).catch(function(error){
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>
.title{
  position: relative;
  width:100%;
  border-bottom: 1px solid #ddd;
  padding: 10% 0;
}
.title a {
  color: black;
  text-decoration: none;
}
.exit{
  position: absolute;
  bottom: 15%;
  right: 0;
  cursor: pointer;
  color:#999;
  text-align:right
}
.pyq{
  padding:10% 10% 10% 15%;
  min-height: 20vh;
  border-bottom: 1px solid #ddd;
  display:flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-start;
}
.delete{
  cursor: pointer;
  color:red;
}
.comment_operator{
  cursor: pointer;
  color:#4a77ad;
  margin-right:2%;
}
.comment{
  font-size: 13px;
  color: #67687c;
  width: 100%;
  background: #f7f7f7;
  padding:4%;
}
.commentInput{
  margin: 10% 0;
  width: 100%;
  outline-style: none;
  border: 1px solid #ccc; 
  border-radius: 3px;
  padding: 7px 0px;
  font-size: 13px;
}
input:focus{
  border-color: #4a77ad;
  outline: 0;
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075),0 0 1px rgba(102,175,233,.6)
}
.sendBtn{
  display: inline-block;
  width: 20%;
  height: 28px;
  line-height: 28px;
  color: #fff;
  background: #01a847;
  border-radius: 6px;
  text-align: center;
  cursor: pointer;
  font-size: 13px;
  margin-left: 2%;
}
</style>