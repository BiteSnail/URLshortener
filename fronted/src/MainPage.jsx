import { useState } from "react";
import * as React from "react";
import axios from "axios";
import Avatar from "@mui/material/Avatar";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import Link from "@mui/material/Link";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import CompressOutlinedIcon from "@mui/icons-material/CompressOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import Button from "@mui/material/Button";
import Backdrop from "@mui/material/Backdrop";
import CircularProgress from "@mui/material/CircularProgress";

const theme = createTheme();

export const Profile = () => {
  return (
    <Box
      sx={{
        marginTop: 2,
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
      }}
    >
      <div>
        <h6>INFO</h6>
        <p>made by bitesnail</p>
        <p>email : rkwoal216@gmail.com</p>
      </div>
    </Box>
  );
};

export const MainPage = () => {
  const [URL, setURL] = useState("Input Your Url");

  const isRightURL = (urlData) => {
    //TODO : require auth for to urlData
    return true;
  };

  const inputHandler = (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      onClickButton();
    }
  };

  const onClickButton = () => {
    axios.interceptors.request.use(
      function (config) {
        handleToggle();
        return config;
      },
      function (error) {
        return Promise.reject(error);
      }
    );

    axios.interceptors.response.use(
      function (response) {
        handleClose();
        return response;
      },
      function (error) {
        return Promise.reject(error);
      }
    );
    // if the interceptors is out from function,
    // the delay is longer for each request. why?

    console.log(URL);
    if (!isRightURL(URL)) {
      return;
    } else {
      axios
        .post("http://localhost:8000/exchange/", {
          origin_url: URL,
        })
        .then(function (response) {
          console.log(response.data.shorten_url, "shorten url");
          setURL(response.data.shorten_url);
        })
        .catch(function (error) {
          console.log(error, "error");
        });
    }
  };

  const [open, setOpen] = React.useState(false);
  const handleClose = () => {
    setOpen(false);
  };
  const handleToggle = () => {
    setOpen(!open);
  };

  const handleCopyClipBoard = async () => {
    try {
      await navigator.clipboard.writeText(URL);
      alert("클립보드에 링크가 복사되었습니다.");
    } catch (e) {
      alert("복사에 실패하였습니다");
    }
  };

  return (
    <Container maxWidth="sm">
      <ThemeProvider theme={theme}>
        <Container component="main" maxWidth="xs">
          <CssBaseline />
          <Box
            sx={{
              marginTop: 2,
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
            }}
          >
            <Avatar sx={{ m: 5, bgcolor: "primary.main" }}>
              <CompressOutlinedIcon />
            </Avatar>
            <Typography component="h1" variant="h5">
              URL Shorter by BiteSnail
            </Typography>
            <Box component="form" onSubmit={() => 0} noValidate sx={{ mt: 1 }}>
              <TextField
                margin="normal"
                required
                fullWidth
                id="url"
                label="Url"
                name="url"
                value={URL}
                variant="outlined"
                onChange={(e) => setURL(e.target.value)}
                autoComplete="email"
                autoFocus
                onKeyPress={(e) => {
                  inputHandler(e);
                }}
              />
              <Button fullWidth variant="contained" onClick={onClickButton} sx={{ mt: 3, mb: 1 }}>
                URL 단축
              </Button>
              <Button
                fullWidth
                variant="contained"
                onClick={handleCopyClipBoard}
                sx={{ bgcolor: "text.secondary", mt: 1, mb: 2 }}
              >
                URL 복사
              </Button>
              <Backdrop
                sx={{ color: "#fff", zIndex: (theme) => theme.zIndex.drawer + 1 }}
                open={open}
                onClick={handleClose}
              >
                <CircularProgress color="inherit" />
              </Backdrop>
              <Grid container>
                <Grid item xs>
                  <Link href="#" variant="body2">
                    Do you want me?
                  </Link>
                </Grid>
              </Grid>
            </Box>
          </Box>
        </Container>
      </ThemeProvider>
      <nav></nav>
      <Profile> </Profile>
    </Container>
  );
};
