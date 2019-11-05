<template>
  <transition name="fade">
    <div class="modal-backdrop">
      <div class="modal">
          <div class="modal-header">
            {{title}}
          </div>
          <div class="modal-body">
              {{content}}
          </div>
          <div class="modal-footer">
              <button type="button" class="btn-close" @click="close" v-if="showCancle">{{cancleText?cancleText : '取消'}}</button>
              <button type="button" class="btn-confirm" @click="confirm">{{confirmText ? confirmText : '确定'}}</button>
          </div>
      </div>
    </div>
  </transition>
</template>
<script>
export default {
  name: 'modal',
  props: {
    // midal标题
    title:{
      type: String,
      default: '提示'
    },
    // modal内容
    content: {
      type: String,
      default: ''
    },
    // 是否显示
    show: {
      type: Boolean,
      default: true
    },
    // 是否显示取消按钮
    showCancle: {
        type: Boolean,
        default: true
    },
    // 确认按钮文字
    confirmText: {
        type: String,
        default: '确认'
    },
    // 取消按钮文字
    cancleText: {
        type: String,
        default: '取消'
    }
  },
  data() {
    return {       
    }
  },
  methods: {
    // 关闭按钮事件
    close() {
        this.$emit('on-cancel');
    },
    // 确定按钮事件
    confirm() {
        this.$emit('on-confirm');
    }
  }
}
</script>
<style>
.modal-backdrop { 
    position: fixed; 
    top: 0; 
    right: 0; 
    bottom: 0; 
    left: 0; 
    background-color: rgba(0,0,0,0.1); 
    width: 100%;
    height: 100%;
    display: flex; 
    justify-content: center; 
    align-items: center; 
    z-index: 99999999;
    
}
.modal { 
    background-color: #fff; 
    overflow-x:auto; 
    display: flex; 
    flex-direction: column;
    border-radius: 16px;
    width: 80%;
} 
.modal-header { 
    color: #313131; 
    justify-content: space-around;
    padding: 15px; 
    display: flex;
    font-size: 24px; 
} 
.modal-footer { 
    border-top: 1px solid #eee; 
    padding: 15px; 
    display: flex; 
    justify-content: space-around;
    align-items: center;
} 
.modal-body { 
    position: relative; 
    padding: 20px; 
    font-size: 20px;
    text-align: center;
}
.btn-close, .btn-confirm {    
    border-radius: 8px;
    border:none;
    cursor: pointer;
    font-size: 20px;
    padding: 5px 15px;
}
.btn-close {
    color: #313131;
    background-color: transparent;
}
.btn-confirm {
    color: #4a77ad; 
    /* background-color: #2d8cf0; */
    background-color: transparent;
}
</style>