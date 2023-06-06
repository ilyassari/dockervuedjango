<template>
  <div class="container">
    <h2> Yeni Yazı Girişi </h2>

    <form @submit.prevent="submitForm">
      <div class="field">
          <label> Başlık </label>
          <div class="control">
              <input type="text" class="input form-control" v-model="title" />
          </div>
      </div>
      <div class="field">
          <label> İçerik </label>
          <div class="control">
              <textarea class="form-control" cols="30" rows="10" v-model="content" ></textarea>
          </div>
      </div>

      <div class="notification is-danger" v-if="errors.length">
          <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
      </div>

      <div class="field">
          <div class="control">
              <button class="btn btn-primary btn-lg">Yazı Ekle</button>
          </div>
      </div>

    </form>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'ArticleCreate',
    data() {
      return {
        title: '',
        content: '',
        errors: []
      }
    },
    components: {
    },
    mounted(){
    },
    methods: {
      submitForm(){
        this.errors = []
        if (this.title === '') {
          this.errors.push('Başlık doldurulmamış')
        } 
        if (this.content === '') {
          this.errors.push('İçerik doldurulmamış')
        }
        if (!this.errors.length) {
          const formData = {
            title: this.title,
            content: this.content
          }
          axios
            .post("/api/article/create", formData)
            .then(response => {
              this.$router.push('/articlelist')
          })
        }
      }
    },
    filters: {
    },
  }
  
</script>
