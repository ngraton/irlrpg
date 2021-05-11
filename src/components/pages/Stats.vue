<template>
  <div>
    <h1>Stats</h1>
    <table>
      <thead>
        <tr>
          <th></th>
          <th>Stat</th>
          <th>Score</th>
        </tr>
      </thead>
      <tbody v-for="(stats, key) in statSheet" :key="key">
        <tr v-for="(stat, name) in stats" :key="name">
          <th v-if="Object.keys(stats)[0] === name " :rowspan="Object.keys(stats).length">{{key.toUpperCase()}}</th>
          <th>{{name}}</th>
          <td>{{stat}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
table {
  border-collapse: collapse;
  border: 2px solid #e7e43b;
  table-layout: fixed;
}

td, th {
    border: 2px solid #e7e43b;
}

</style>

<script>
export default {
  name: 'Stats',
  data () { return {
    statSheet: {
      body: {
        STR: 6,
        END: 6
      },
      mind: {
        INT: 9,
        WIS: 6
      },
      soul: {
        CON: 6,
        CHA: 5,
        SPT: 5
      }
    }
  }}
}
</script>