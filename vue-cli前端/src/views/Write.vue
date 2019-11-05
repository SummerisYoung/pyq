<template>
    <div>
        <div class="top">
            <img style="margin-right:10px" src="../assets/back.png" alt="" @click="backPyq()">
            <span>发表朋友圈</span>
        </div>
        <textarea v-model="content" class="write" name="write" placeholder="这一刻的想法..."></textarea>
        <input type="submit" value="发表" @click="writePyq()">
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return {
            content:'',//朋友圈
            time:'',//时间
        }
    },
    methods:{
        backPyq(){//返回朋友圈页面
            this.$router.push({
                name:'pyq'
            })
        },
        writePyq(){//新增朋友圈
            var now = new Date()
            var t = now.getFullYear() + '-' + (now.getMonth() + 1) + '-' + now.getDate() + ' '
             + now.getHours() + ':' + now.getMinutes() + ':' + now.getSeconds()
            var that = this
            axios.post('http://127.0.0.1:8000/app/pyq',{
                userid:localStorage.userid,
                content:that.content,
                time:t
            }).then(function(res){
                console.log(res)
                if(res.data="add success!"){
                    alert("发表成功！")
                    that.$router.push({
                        name:'pyq',
                    })
                }else{
                    alert("发表失败！")
                }
            }).catch(function(error){
                console.log(error)
            })
        }
    }
}
</script>

<style scoped>
.top{
    text-align: left;
    margin: 30px 0;
    font-weight: 500;
    display: flex;
}
.write{
    width: 100%;
    border: none;
    min-height: 20vh;
    outline:none;
    resize:none;
}
</style>