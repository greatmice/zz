package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log/slog"
	"net/http"
)

type Response struct {
	Anime string `json:"type"`
}

func Jikan() string {
	resp, err := http.Get("https://api.jikan.moe/v4/random/anime")
	if err != nil {
		slog.Error(err.Error())
	}
defer resp.Body.Close()

    body, err := io.ReadAll(resp.Body)
	if err != nil {
		slog.Error(err.Error())
	} 

    var data Response
	if err := json.Unmarshal(body, &data); err != nil {
		slog.Error(err.Error())
   }
    if data.Anime == "TV" {
		fmt.Println(data.Anime)
    }
     return data.Anime
}

func main() {
	fmt.Println(Jikan())
}