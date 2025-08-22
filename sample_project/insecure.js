// intentional insecure JS for scanner demonstration
const password = "supersecret";
console.log("Password is", process.env.PASSWORD);
eval("console.log('danger')");
