<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Policies</h1>
        <hr><br><br>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Time</th>
              <th scope="col">Articles</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(policy, index) in policies" :key="index">
              <td>{{ policy.title[0] }}</td>
              <td>{{ policy.time[0] }}</td>
              <td>{{ policy.article }}</td>
              <td>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      policies: [],
    };
  },
  methods: {
    getPolicies() {
      const path = 'http://localhost:5000/policies';
      axios.get(path)
        .then((res) => {
          this.policies = res.data.policies;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getPolicies();
  },
};
</script>
