const express = require('express')
const app = express()
const port = 3008

app.get('/', (req, res) => res.json([
    {
        name: 'Chin',
        email: 'chint.c@gmail.com'
    },
    {
        name: 'Chint',
        email: 'chinta.c@gmail.com'
    },
    {
        name: 'Chinta',
        email: 'chintam.c@gmail.com'
    },
    {
        name: 'Chintam',
        email: 'chintama.c@gmail.com'
    }
]))

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})