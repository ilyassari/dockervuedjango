<template>
  <div class="container">
    <h1>Yazılar</h1>
    <div class="row row-cols-1 row-cols-md-3 g-4">
      <div 
        class="col" 
        style="width: 18rem;"
        v-for="article in articles"
        v-bind:key="article.id"
      >
        <div class="card">
          <div class="card-body">
            <h5 class="card-title"> {{ article.title }} </h5>
            <p class="card-text"> {{ article.content.split(" ").splice(0,20).join(" ") }} </p>
            <a :href="`/article/${article.id}`" class="btn btn-primary btn-sm">Devamı...</a>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'ArticleList',
    data() {
      return{
        articles: []
      }
    },
    components: {
    },
    mounted(){
      this.getArticles()
    },
    methods: {
      getArticles() {
        axios
          .get('/api/article/list')
          .then(response => {
            this.articles = response.data
          })
          .catch(error => {
            console.log(error);
          })
      }
    },
    filters: {
      capitalize: function (value) {
        if (!value) return ''
        value = value.toString()
        return value.charAt(0).toUpperCase() + value.slice(1)
      },      
      truncate: function(data, num){
        return data.split(" ").splice(0,3).join(" ");
      }
    },
  }
  
</script>
