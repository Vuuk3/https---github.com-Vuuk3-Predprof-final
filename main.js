const config = {
    baseUrl: "https://nomoreparties.co/v1/wff-cohort-8",
    headers: {
      "Content-Type": "application/json",
    },
  };

const getSh = () => {
    return fetch(`${config.baseUrl}/zvo/sh`, {
        headers: config.headers
    }).then((res) => {
        if (res.ok) {
            return res.json()
        }
        return Promise.reject(`Ошибка ${res.status}`)
    })
}

getSh().then((res) => {console.log(res)})
