<template>
  <div class="container">
    <h1>{{ article.title }}</h1>
    <p>
      {{ article.content }}
    </p>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'ArticleDetail',
    data() {
      return{
        articleId: 1,
        article: {},
      }
    },
    components: {
    },
    mounted(){
      this.getArticle()
    },
    methods: {
      getArticle() {
        const articleId = this.$route.params.articleId
        axios
          .get(`/api/article/detail/${articleId}`)
          .then(response => {
            this.article = response.data
          })
          .catch(error => {
            console.log(error);
          })
      }
    },
    filters: {
      capitalising: function (data) {
        var capitalized = []
        data.split(' ').forEach(word => {
          capitalized.push(
            word.charAt(0).toUpperCase() +
            word.slice(1).toLowerCase()
          )
        })
        return capitalized.join(' ')
      }
    },
  }
  
</script>
